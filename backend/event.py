class Time():
  def __init__(self, year, month, day, hour):
    self.year = year
    self.month = month
    self.day = day
    self.hour = hour

class Event():
  def __init__(self, start_time, end_time):
    self.start_time = start_time
    self.end_time = end_time
