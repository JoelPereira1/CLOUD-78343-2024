import uuid

TABLENAME = 'tblPosts'

class Post:
  # função construtora
  def __init__(self, id, customer_id, response, daily_id = '', chat_id = '', IsCosmos = False):
    self.id = id
    self.customer_id = customer_id
    self.response = response
    self.daily_id = daily_id
    self.chat_id = chat_id

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
