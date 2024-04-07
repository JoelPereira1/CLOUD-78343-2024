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
    return f"{self.review}  {self.rating}"

  def plants_reviews():
    # return all reviews for plants
    pass

  def orders_reviews():
    # return all reviews for orders
    pass

  def user_reviews(user_id):
    # return all reviews for user
    pass

