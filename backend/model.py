from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date, timedelta

class Model():
    def __init__(self, connection=('localhost', 27017)):
        client = MongoClient(*connection)
        self.communities = client['syncsoc']['communities']
        self.days = client['syncsoc']['days']
        self.events = client['syncsoc']['events']

    def add_community(self, community_name, mailingList):
        self.communities.insert_one({'name': community_name, 'mailingList': mailingList})


    def add_event(self, community_id, date, start_slot, end_slot):
        event = {'comm_id': community_id, 'date': str(date), 'start': start_slot, 'end': end_slot}
        self.events.insert_one(event)
        event_id = self.events.find_one({'comm_id': community_id, 'date': str(date), 'start': start_slot, 'end': end_slot})['_id']
        try:
            target_day = self.days.find_one({'date': str(date)})
            day_id = target_day['_id']
            slots = target_day['slots']
            for i in range(start_slot, end_slot):
                slots[i] += [str(event_id)]
            self.days.find_one_and_update({"_id": day_id}, 
                                 {"$set": {"slots": slots}})
        except:
            print('fix week day!!!')
            new_day = {'weekDay': 'Monday', 'date': str(date), 'slots': [[] for i in range(48)]}
            for i in range(start_slot, end_slot):
                new_day['slots'][i] += [event_id]

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
        day = {'weekDay': day_date.weekday(), 'date': str(day_date), 'slots': [[] for i in range(48)]}
        self.days.insert_one(day)
    
def _daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
