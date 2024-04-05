# from flask_wtf import FlaskForm
# from wtforms import StringField, IntegerField, SubmitField
# from wtforms.validators import DataRequired, Length
# from wtforms.validators import DataRequired, Length, Regexp
# from wtforms.fields import *

class StopValidation(Exception):
  """
  Causes the validation chain to stop.

  If StopValidation is raised, no more validators in the validation chain are
  called. If raised with a message, the message will be added to the errors
  list.
  """

  def __init__(self, message="", *args, **kwargs):
    Exception.__init__(self, message, *args, **kwargs)

class DataRequired:
  """
  Checks the field's data is 'truthy' otherwise stops the validation chain.

  This validator checks that the ``data`` attribute on the field is a 'true'
  value (effectively, it does ``if field.data``.) Furthermore, if the data
  is a string type, a string containing only whitespace characters is
  considered false.

  If the data is empty, also removes prior errors (such as processing errors)
  from the field.

  **NOTE** this validator used to be called `Required` but the way it behaved
  (requiring coerced data, not input data) meant it functioned in a way
  which was not symmetric to the `Optional` validator and furthermore caused
  confusion with certain fields which coerced data to 'falsey' values like
  ``0``, ``Decimal(0)``, ``time(0)`` etc. Unless a very specific reason
  exists, we recommend using the :class:`InputRequired` instead.

  :param message:
      Error message to raise in case of a validation error.

  Sets the `required` attribute on widgets.
  """

  def __init__(self, message=None):
    self.message = message
    self.field_flags = {"required": True}

  def __call__(self, form, field):
    if field.data and (not isinstance(field.data, str) or field.data.strip()):
        return

    if self.message is None:
        message = field.gettext("This field is required.")
    else:
        message = self.message

    field.errors[:] = []
    raise StopValidation(message)

def _required(form, field):
  pass
  # if not form.submit_pre.data:
  #   field.validators.append(DataRequired())
  #   match field.id:
  #     case 'nim':
  #       field.validators.append(Length(0, 10, 'Can be interpolated using %(min)d and %(max)d'))
  #     case 'cc':
  #       field.validators.append(Length(8, 10, 'Can be interpolated using %(min)d and %(max)d'))
  #     case 'nome':
  #       field.validators.append(Length(2, 20, 'Can be interpolated using %(min)d and %(max)d'))
  #     case 'apelido':
  #       field.validators.append(Length(3, 20, 'Can be interpolated using %(min)d and %(max)d'))
  #     case 'patente':
  #       field.validators.append(Length(3, 20, 'Can be interpolated using %(min)d and %(max)d'))