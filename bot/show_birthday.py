from colorama import Fore
from models import AddressBook


def input_error(func):
  def inner(*args, **kwargs) -> str:
    try:
      return func(*args, **kwargs)
    except (ValueError, IndexError):
      return f'{Fore.YELLOW}Please provide contact name{Fore.RESET}'
    except AttributeError:
      return f'Record "{args[0][0]}" has no birthday'
  return inner


@input_error
def show_birthday(args: str, book: AddressBook) -> str:
  name, *_ = args
  record = book.find_record(name)
  if record:
    return record.birthday.value.strftime('%d.%m.%Y')
  return f'There is no contact named {name}'
