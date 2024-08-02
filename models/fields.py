import re
from datetime import datetime


class Field:
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return str(self.value)


class Name(Field):
  def __init__(self, value: str):
    self.value = value


class Phone(Field):
  def __init__(self, value: str):
    super().__init__(value)
    self.validate_phone()

  def validate_phone(self) -> None:
    match = re.match(r'^\d{10}$', self.value)
    if not match:
      raise ValueError

  def __eq__(self, other: object) -> bool:

    if isinstance(other, Phone):
      return self.value == other.value
    if isinstance(other, str):
      return self.value == other
    return False


class Birthday(Field):
  def __init__(self, value):

    try:
      self.value = datetime.strptime(value, '%d.%m.%Y').date()
    except ValueError:
      raise ValueError
