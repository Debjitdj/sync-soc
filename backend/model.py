from pymongo import MongoClient
from bson.objectid import ObjectId

class Model():
    def __init__(self, connection=('localhost', 27017)):
        client = MongoClient(*connection)
        self.communities = client['syncsoc']['communities']
        self.days = client['syncsoc']['days']
        self.events = client['syncsoc']['events']


    def add_event(self, community_id, date, start_slot, end_slot):
        event = {'comm_id': community_id, 'date': date, 'start': start_slot, 'end': end_slot}
        self.events.insert_one(event)
        event_id = self.events.find_one({'comm_id': community_id, 'date': date, 'start': start_slot, 'end': end_slot})['_id']
        try:
            target_day = self.days.find_one({'date': date})
            day_id = target_day['_id']
            slots = target_day['slots']
            for i in range(start_slot, end_slot):
                slots[i] += [str(event_id)]
            self.days.find_one_and_update({"_id": day_id}, 
                                 {"$set": {"slots": slots}})
        except:
            print('fix week day!!!')
            new_day = {'weekDay': 'Monday', 'date': date, 'slots': [[] for i in range(48)]}
            for i in range(start_slot, end_slot):
                new_day['slots'][i] += [event_id]

    def remove_event(self, event_id):
        event = self.events.find_one({'_id':ObjectId(event_id)})
        day = self.days.find_one({'date':event['date']})
        slots = day['slots']
        day_id = day['_id']
        try:
            for i in range(event['start'], event['end']):
                slots[i].remove(event_id)
        except ValueError():
            print('Event not in the list!')
        self.days.find_one_and_update({"_id": day_id}, 
                                 {"$set": {"slots": slots}})
        


        
