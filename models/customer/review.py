import uuid

TABLENAME = 'tblReviews'

class Review:
  # função construtora
  def __init__(self, id, customer_id, plant_id, order_id, review, rating, IsCosmos):
    self.id = id
    self.customer_id = customer_id
    self.plant_id = plant_id
    self.order_id = order_id
    self.review = review
    self.rating = rating

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
