from models import AddressBook


def upcoming_birthdays(book: AddressBook) -> str:
  upcoming_birthdays = book.get_upcoming_birthdays()
  if not upcoming_birthdays:
    return 'No upcoming birthdays'
  return '\n'.join([f'{record["name"]} - {record["congratulation_date"]}' for record in upcoming_birthdays])
