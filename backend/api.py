import flask, model
from flask import request, jsonify
import datetime
from bson.objectid import ObjectId

app = flask.Flask(__name__)
app.config["DEBUG"] = True

model = model.Model()
communities = list(model.communities.find())
days = list(model.days.find())
events = list(model.events.find())

#front -> back
@app.route('/add_event', methods = ['GET'])
def add_event():
  community_name = request.args.get('name')
  
  year = request.args.get('year')
  month = request.args.get('month')
  day = request.args.get('day')
  try:
    date = datetime.date(year, month, day)
  except:
    print('using default date of (2019, 10, 2)')
    date = datetime.date(2019, 10, 2)

  start_slot = request.args.get('start_slot')
  end_slot = request.args.get('end_slot')
  if community_name is None:  # test
    community_name = 'Sync Society'
    start_slot = 20
    end_slot = 25

  community = model.communities.find_one({"name" : community_name})
  
  weekly = request.args.get('weekly')
  print(weekly)
  if not weekly:
    model.add_event(community["_id"], date, start_slot, end_slot)
  else:
    model.add_recurring_event(community["_id"], date.weekday(), start_slot, end_slot)
    print('adding recurring event')
  return jsonify(True)

@app.route('/add_community', methods = ['GET']) 
def add_community():
  community_name = request.args.get('name')
  mails = request.args.get('mails').split(', ')
  password = request.args.get('password')

  # some default values
  if community_name is None:
    community_name = "A nameless society"
  if mails is None:
    mails = []
  if password is None:
    password = ""
  
  model.add_community(community_name, mails, password)

  return jsonify(True)
  
#back -> front

@app.route('/get_calendar', methods = ['GET'])
def get_calendar():
  community_name = request.args.get('name')
  if community_name is None: community_name = 'Sync Society'
  community = model.communities.find_one({"name" : community_name})
  year = request.args.get('year')
  month = request.args.get('month')
  day = request.args.get('day')
  try:
    start_date = datetime.date(year, month, day)
  except:
    start_date = datetime.date(2019, 10, 1)

  our_mails = community["mailing_list"]

  model.assert_days_present(start_date, start_date + datetime.timedelta(days=7))


  # non-recurring events

  calendar = [[[] for i in range(48)] for j in range(7)]
  for i in range(7):
    date = start_date + datetime.timedelta(days=i)
    db_day = model.days.find_one({"date": str(date)})

    for db_slot, cal_slot in zip(db_day["slots"], calendar[i]):
      for event_id in db_slot:
        event = model.events.find_one({"_id":ObjectId(event_id)})
        comm_id = event["comm_id"]
        print(comm_id)
        other_community = model.communities.find_one({"_id":ObjectId(str(comm_id))})

        for mail in other_community["mailing_list"]:
          if mail in our_mails:
            cal_slot += [mail]

  # recurring events

  recurring_events = list(model.recurring_events.find())
  for event in recurring_events:
    week_day = event["week_day"]
    start_slot = event["start"]
    end_slot = event["end"]

    comm_id = event["comm_id"]
    print(str(comm_id))
    other_community = model.communities.find_one({"_id": ObjectId(str(comm_id))})
    for mail in other_community["mailing_list"]:
      for i in range(start_slot, end_slot):
        if mail in our_mails:
          calendar[week_day][i] += [mail]

  # computing actual results

  result = [[0 for i in range(48)] for j in range(7)]

  for i in range(7):
    for j in range(48):
      result[i][j] = float(len(set(calendar[i][j]))) / float(len(our_mails))

  return jsonify(result)
  
