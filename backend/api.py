import flask, model
from flask import request, jsonify

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
  date = request.args.get('date')
  start_slot = request.args.get('start_slot')
  end_slot = request.args.get('end_slot')

  model.assert_days_present(date, date)
  community = model.communities.find_one({"name" : community_name})
  model.add_event(community["_id"], date, start_slot, end_slot)  

#back -> front

@app.route('/get_calendar', methods = ['GET'])
def get_calendar():
  community_name = request.args.get('name')
  community = model.communities.find_one({"name" : community_name})
  start_date = request.args.get('date')

  our_mails = community["mailing_list"]

  calendar = [[[] for i in range(48)] for j in range(7)]
  for i in range(7):
    date = start_date + datetime.timedelta(days=i)
    db_day = model.days.find_one({"date" : str(date)})

    for db_slot, cal_slot in zip(db_day["slots"], calendar[i]):
      for event_id in db_slot:
        event = model.events.find_one({"_id":ObjectId(event_id)})
        comm_id = event["comm_id"]
        other_community = model.events.find_one({"_id":ObjectId(comm_id)})

        for mail in other_community["mailing_list"]:
          if our_mails.contains(mail):
            cal_slot += [mail]

  result = [[0 for i in range(48)] for j in range(7)]

  for i in range(7):
    for j in range(48):
      result[i][j] = double(set(calendar[i][j]).size) / double(our_mails.size)

  return jsonify(result)
  
