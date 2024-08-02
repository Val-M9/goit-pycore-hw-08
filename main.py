from bot import (
    add_contact,
    show_all,
    show_phone,
    change_contact,
    parse_input,
    add_birthday,
    show_birthday,
    upcoming_birthdays,
    all_commands,
    exit_commands,
)
from helpers import load_data, save_data
from constants import FILENAME


def main():
  book = load_data(FILENAME)
  print('Welcome to assistance bot!')

  while True:
    user_input = input('Enter a command: ')
    command, *args = parse_input(user_input)

    match command:
      case _ if command in exit_commands:
        save_data(book, FILENAME)
        print('Good bye!')
        break
      case 'hello':
        print('How can I help you?')
      case 'add':
        print(add_contact(args, book))
      case 'all':
        print(show_all(book))
      case 'phone':
        print(show_phone(args, book))
      case 'change':
        print(change_contact(args, book))
      case 'add-birthday':
        print(add_birthday(args, book))
      case 'show-birthday':
        print(show_birthday(args, book))
      case 'birthdays':
        print(upcoming_birthdays(book))
      case _:
        print(f'Invalid command. Here is the list of available commands: {
              all_commands}')


if __name__ == '__main__':
  main()
