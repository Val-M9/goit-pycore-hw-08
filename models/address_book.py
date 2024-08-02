from collections import UserDict
from datetime import datetime
from .record import Record


class AddressBook(UserDict):
  def __str__(self):
    return '\n'.join([str(record) for record in self.data.values()])

  def add_record(self, record: Record):
    self.data[record.name] = record

  def find_record(self, name: str) -> None:
    for record_name in self.data.keys():
      if str(record_name) == name:
        return self.data[record_name]

  def delete(self, name: str) -> None:
    for record_name in self.data.keys():
      if str(record_name) == name:
        self.data.pop(record_name)
        print(f'Contact {name} has been deleted')
        break
    else:
      print(f'Contact {name} was not found')

  def get_upcoming_birthdays(self) -> list[dict]:
    today = datetime.today().date()
    congratulation_list = []
    for name, record in self.data.items():
      if not record.birthday:
        continue
      birthday_this_year = record.birthday.value.replace(
          year=datetime.now().year)
      birthday_next_year = record.birthday.value.replace(
          year=datetime.now().year + 1)
      upcoming_birthday = birthday_this_year if birthday_this_year >= today else birthday_next_year

      if (upcoming_birthday - today).days >= 0 and (upcoming_birthday - today).days <= 7:
        if upcoming_birthday.isoweekday() == 6:
          congratulation_day = upcoming_birthday.replace(
              day=upcoming_birthday.day + 2)
          congratulation_list.append(
              {'name': name.value, 'congratulation_date': datetime.strftime(congratulation_day, '%d.%m.%Y')})

        elif upcoming_birthday.isoweekday() == 7:
          congratulation_day = upcoming_birthday.replace(
              day=upcoming_birthday.day + 1)
          congratulation_list.append(
              {'name': name.value, 'congratulation_date': datetime.strftime(congratulation_day, '%d.%m.%Y')})

        else:
          congratulation_list.append(
              {'name': name.value, 'congratulation_date': datetime.strftime(upcoming_birthday, '%d.%m.%Y')})

    return congratulation_list
