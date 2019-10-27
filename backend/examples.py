one_day = {'weekDay':'Monday', 'date':'01/11/2019', 'slots' : [[] for i in range(48)]]}  # empty list for ids of events

event = {'socId':'0', 'date': '01/11/2019', 'start': 30, 'end': 35}

community = {'mailingList': []}

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