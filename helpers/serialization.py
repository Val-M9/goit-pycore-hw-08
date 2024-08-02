import pickle

from models import AddressBook


def save_data(book: AddressBook, filename: str):
  with open(filename, 'wb') as file:
    pickle.dump(book, file)


def load_data(filename: str) -> AddressBook:
  try:
    with open(filename, 'rb') as file:
      return pickle.load(file)
  except FileNotFoundError:
    return AddressBook()
