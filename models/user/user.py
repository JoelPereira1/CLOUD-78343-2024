import uuid

TABLENAME = 'tblUsers'

class User:
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


#   @hybrid_property
#   def password(self):
#       return self._password

#   @password.setter
#   def password(self, value):
#       self._password = bcrypt.generate_password_hash(value).decode("UTF-8")

#   @property
#   def avatar(self):
#       return Gravatar(self.email).get_image()

#   def check_password(self, value):
#       """Check password."""
#       return bcrypt.check_password_hash(self.password.encode("utf-8"), value)

#   @property
#   def addresses(self):
#       return UserAddress.query.filter_by(user_id=self.id).all()

#   @property
#   def is_active_human(self):
#       return "Y" if self.is_active else "N"

#   @property
#   def roles(self):
#       at_ids = (
#           UserRole.query.with_entities(UserRole.role_id)
#           .filter_by(user_id=self.id)
#           .all()
#       )
#       return Role.query.filter(Role.id.in_(id for id, in at_ids)).all()

  def delete(self):
      for addr in self.addresses:
          addr.delete()
      return super().delete()

  def can(self, permissions):
      if not self.roles:
          return False
      all_perms = reduce(or_, map(lambda x: x.permissions, self.roles))
      return all_perms >= permissions

  def can_admin(self):
      return self.can(Permission.ADMINISTER)

  def can_edit(self):
      return self.can(Permission.EDITOR)

  def can_op(self):
      return self.can(Permission.OPERATOR)