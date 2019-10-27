class Community():
  def __init__(self, users, idd):
    self.users = users
    self.id = idd
    self.events = []

  def compare_community(self, Community other):
    # returns intersection of two societies.

class User():
  def __init__(self, email):
    self.email = email
