def parse_input(user_input: str) -> tuple:
  command, *args = user_input.split()
  command = command.strip().lower()

  return command, *args
