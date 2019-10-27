from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date, timedelta

class Model():
    def __init__(self, connection=('localhost', 27017)):
        client = MongoClient(*connection)
        self.communities = client['syncsoc']['communities']
        self.days = client['syncsoc']['days']
        self.events = client['syncsoc']['events']
        self.recurring_events = client['syncsoc']['recurring_events']

    def add_community(self, community_name, mailing_list, owner_email='a@a', password='abc123'):
        self.communities.insert_one({'name': community_name, 'mailing_list': mailing_list, 'password': password, 'owner_email': owner_email})

    def get_community_id(self, community_name):
        try:
            return self.communities.find_one({'name': community_name})['_id']
        except KeyError():
            print('NO COMMUNITY')


    def add_event(self, community_id, day_date, start_slot, end_slot):
        event = {'comm_id': community_id, 'date': str(day_date), 'start': start_slot, 'end': end_slot}
        self.events.insert_one(event)
        event_id = self.events.find_one({'comm_id': community_id, 'date': str(day_date), 'start': start_slot, 'end': end_slot})['_id']
        try:
            target_day = self.days.find_one({'date': str(day_date)})
            day_id = target_day['_id']
            slots = target_day['slots']
            for i in range(start_slot, end_slot):
                slots[i] += [str(event_id)]
            self.days.find_one_and_update({"_id": day_id}, 
                                 {"$set": {"slots": slots}})
        except KeyError():  # this should not happen ever!
            print('fix week day!!!')
            new_day = {'week_day': 'Monday', 'date': str(day_date), 'slots': [[] for i in range(48)]}
            for i in range(start_slot, end_slot):
                new_day['slots'][i] += [event_id]

    def add_recurring_event(self, community_id, week_day, start_slot, end_slot):
        event = {'comm_id': community_id, 'week_day': week_day, 'start': start_slot, 'end': end_slot}
        self.recurring_events.insert_one(event)

    def remove_event(self, event_id):
        event = self.events.find_one({'_id': ObjectId(event_id)})
        day = self.days.find_one({'date': event['date']})
        slots = day['slots']
        day_id = day['_id']
        try:
            for i in range(event['start'], event['end']):
                slots[i].remove(event_id)
        except ValueError():
            print('Event not in the list!')
            return False
        self.days.find_one_and_update({"_id": day_id},
                                 {"$set": {"slots": slots}})

        self.events.delete_one({'_id': ObjectId(event_id)})
        
    def assert_days_present(self, start_date, end_date):
        for day_date in _daterange(start_date, end_date):
            if self.days.find_one({'date': str(day_date)}) is None:
                self._add_day(day_date)
        
    def _add_day(self, day_date):
        day = {'week_day': day_date.weekday(), 'date': str(day_date), 'slots': [[] for i in range(48)]}
        self.days.insert_one(day)
    
def _daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
