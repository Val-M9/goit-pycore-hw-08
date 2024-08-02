from .fields import Name, Phone, Birthday


class Record:
  def __init__(self, name):
    self.name = Name(name)
    self.phones: list[Phone] = []
    self.birthday: Birthday = None

  def add_phone(self, phone: str) -> bool:
    try:
      valid_phone = Phone(phone)
      self.phones.append(valid_phone)
      return True
    except ValueError as e:
      print(e)
      return False

  def remove_phone(self, phone: str) -> None:
    if not phone in self.phones:
      print(f'Phone number {phone} was not found')
    self.phones.remove(phone)
    print(f'Phone number {phone} has been removed')

  def edit_phone(self, phone: str, new_phone: str) -> None:
    if not phone in self.phones:
      print(f'Phone number {phone} was not found')
    for i, phone_record in enumerate(self.phones):
      if phone_record == phone:
        self.phones[i] = Phone(new_phone)

  def find_phone(self, phone: str) -> None:
    if not phone in self.phones:
      print(f'Phone number {phone} was not found')
    for phone_record in self.phones:
      if phone_record == phone:
        print(f'Phone number {phone} was found')

  def add_birthday(self, birthday: str) -> None:
    try:
      self.birthday = Birthday(birthday)
      return True
    except ValueError as e:
      print(e)
      return False

  def __str__(self):
    return f'Contact name: {self.name.value}, phones: {"; ".join(p.value for p in self.phones)}' \
        f'{", birthday " +
           self.birthday.value.strftime('%d.%m.%Y') if self.birthday else ""}'
