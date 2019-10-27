class Community():
  def __init__(self, users, idd):
    self.users = users
    self.id = idd
    self.events = []

  def compare_community(self, other_community):
    # returns intersection of two societies.

  def add_member(self, member_email):
    pass

class User():
  def __init__(self, email):
    self.email = email
