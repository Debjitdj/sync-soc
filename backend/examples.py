one_day = {'weekDay':'Monday', 'date':'28/10/2019', 'slots' : [[] for i in range(48)]}  # empty list for ids of events

event = {'comm_id':'5db583b03c712161122e94db', 'date': '28/10/2019', 'start': 30, 'end': 35}

community = {'name':'Sync Society', 'mailingList': []}

recurring_event = {'weekDay': 'Monday'}



'''
add_event(self, date, start_slot, end_slot):
    - creates JSON of event
    - adds event ID to list in relevant places
    - returns 0/1

remove_event(self, event_id):
    - frees slots
    
compute_soc(self, soc_id, earliest_day, latest_day)
    - returns the whole table

'''