import uuid

class Oder:
  # função construtora
  def __init__(self, id, email, phone_number, first_name, last_name, user_name, IsCosmos):
    self.id = id
    self.email = email
    self.phone_number = phone_number
    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name

    if id == '':
      if IsCosmos:
        self.id = str(uuid.uuid4())
      else:
        self.id = id
    else:
      self.id = id

  def __str__(self):
    return f"{self.first_name}  {self.last_name}"

  def identification(self):
    return f"{self.email} - {self.user_name}"
