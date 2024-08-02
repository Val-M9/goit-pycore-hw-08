from colorama import Fore
from models import AddressBook, Record


def input_error(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except ValueError:
      return f'Please provide two values: {Fore.YELLOW}name and birthday. ' \
          f'Birthday should be in format "YYYY-MM-DD"{Fore.RESET}'
  return wrapper


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
  name, birthday, *_ = args
  record = book.find_record(name)
  message = f'{Fore.GREEN}Birthday updated!{Fore.RESET}'
  if record is None:
    record = Record(name)
    book.add_record(record)
    message = f'{Fore.GREEN}Birthday added!{Fore.RESET}'
  if not record.birthday:
    message = f'{Fore.GREEN}Birthday added!{Fore.RESET}'
  if birthday:
    added_birthday = record.add_birthday(birthday)
    if not added_birthday:
      raise ValueError
  return message
