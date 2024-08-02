from models import AddressBook


def show_all(book: AddressBook) -> str | AddressBook:
  if not book:
    return 'No records'
  return book
