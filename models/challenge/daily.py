import uuid

TABLENAME = 'tblDailys'

class Dayli:
  # função construtora
  def __init__(self, id, photo, question, IsCosmos):
    self.id = id
    self.photo = photo
    self.question = question

    if id == '':
      if IsCosmos:
        self.id = str(uuid.uuid4())
      else:
        self.id = id
    else:
      self.id = id
