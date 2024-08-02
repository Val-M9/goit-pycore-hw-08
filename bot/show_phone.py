from colorama import Fore
from models import AddressBook


def input_error(func):
  def wrapper(*args, **kwargs):
    try:
      if len(args[0]) > 1:
        raise IndexError
      return func(*args, **kwargs)
    except (IndexError, ValueError):
      return f'Please provide one value:{Fore.YELLOW} name{Fore.RESET}'
    except AttributeError:
      return f'There is no contact named {Fore.YELLOW}{"".join(args[0])}{Fore.RESET}'
  return wrapper


@input_error
def show_phone(args: str, book: AddressBook) -> str:
  name, *_ = args
  record = book.find_record(name)
  return '; '.join(phone.value for phone in record.phones)
