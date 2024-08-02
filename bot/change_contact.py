from colorama import Fore
from models import AddressBook


def input_error(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except ValueError:
      return f'Please provide three values: {Fore.YELLOW}name, an old phone and new phone number{Fore.RESET} \
        New phone should contain 10 digits'
    except AttributeError:
      return f'There is no contact named {Fore.YELLOW}{args[0][0]}{Fore.RESET}'

  return wrapper


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
  name, old_phone, new_phone, *_ = args
  record = book.find_record(name)
  record.edit_phone(old_phone, new_phone)
  return f'{Fore.GREEN}Contact updated!{Fore.RESET}'
