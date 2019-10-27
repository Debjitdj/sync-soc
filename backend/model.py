from pymongo import MongoClient

class Model():
    def __init__(self, connection=('localhost', 27017))):
        client = MongoClient(*connection)
        self.communities = client['syncsoc']['communities']
        self.days = client['syncsoc']['days']
        self.events = client['syncsoc']['events']


    def add_event(self, society_id, date, start_slot, end_slot):
        event = {'socId': }
        events.insert_one()
        
