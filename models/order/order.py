import uuid

class Oder:
  # função construtora
  def __init__(self, id, shipping_address, customer_id, total_net, shipping_price_net, status_id, shipping_method_id, ship_status_id, IsCosmos):
    self.id = id
    self.shipping_address = shipping_address
    self.customer_id = customer_id
    self.total_net = total_net
    self.shipping_price_net = shipping_price_net
    self.status_id = status_id
    self.shipping_method_id = shipping_method_id
    self.ship_status_id = ship_status_id

    if id == '':
      if IsCosmos:
        self.id = str(uuid.uuid4())
      else:
        self.id = id
    else:
      self.id = id

  def __str__(self):
    return f"{self.first_name}  {self.last_name}"

  def plants_orders():
    # return all reviews for plants
    pass

  def orders_reviews():
    # return all reviews for orders
    pass

  def user_reviews(user_id):
    # return all reviews for user
    pass

  @property
  def total(self):
    return self.total_net + self.shipping_price_net

  @property
  def status_human(self):
    return OrderStatusKinds(int(self.status)).name

  @property
  def total_human(self):
    return "€" + str(self.total)

  @classmethod
  def get_current_customer_orders(cls):
    if current_customer.is_authenticated:
        orders = (
            cls.query.filter_by(customer_id=current_customer.id)
            .order_by(Order.id.desc())
            .all()
        )
    else:
        orders = []
    return orders

  @classmethod
  def get_customer_orders(cls, customer_id):
    return cls.query.filter_by(customer_id=customer_id).all()

  @property
  def is_shipping_required(self):
    return any(line.is_shipping_required for line in self.lines)

  @property
  def is_self_order(self):
    return self.user_id == current_user.id