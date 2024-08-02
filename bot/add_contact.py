from colorama import Fore
from models import AddressBook, Record


def input_error(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except ValueError:
      return f'Please provide two values: {Fore.YELLOW}name and phone number. '\
          f'Phone number should contain 10 digits{Fore.RESET}'
  return wrapper


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
  name, phone = args
  record = book.find_record(name)
  message = f'{Fore.GREEN}Contact updated!{Fore.RESET}'
  if record is None:
    record = Record(name)
    book.add_record(record)
    message = f'{Fore.GREEN}Contact added!{Fore.RESET}'
  if phone:
    added_phone = record.add_phone(phone)
    if not added_phone:
      raise ValueError
  return message
