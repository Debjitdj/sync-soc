from pymongo import MongoClient

class Model():
    def __init__(self, connection=('localhost', 27017))):
        client = MongoClient(*connection)
        self.communities = client['syncsoc']['communities']
        self.days = client['syncsoc']['days']
        self.events = client['syncsoc']['events']


    def add_event(self, community_id, date, start_slot, end_slot):
        event = {'comm_id': community_id, 'date': date, 'start': start_slot, 'end': end_slot}
        events.insert_one(event)
        try:
            day_id = days.find_one({'date': date})
        except:
            

        
