def show_game_state(attempts_array, errors):
  print(f"\n{''.join(attempts_array)}")
  print(f"Errors: {errors}\n")

def play_game(secret_word):
  attempts_array = []
  errors = 0
  max_attempts = 6
  won = False
  repeated = False

  for i in secret_word:
    attempts_array.append("_")

  while not won and errors != max_attempts:
    found = False
    guess = input("\n____________________\nGuess: ")

    for i in attempts_array:
      if guess.casefold() == i.casefold():
        print("You can't repeat letters")
        show_game_state(attempts_array, errors)
        repeated = True

    if repeated:
      repeated = False
      continue

    pos = 0
    for i in secret_word:
      if guess.casefold() == i.casefold():
        found = True
        attempts_array[pos] = guess

      pos += 1

    if not found:
      errors += 1

    show_game_state(attempts_array, errors)

    if not "_" in attempts_array:
      won = True
      break

  return won

secret_word = input("Inform the secret word: ")

if play_game(secret_word):
  print("You won")
else:
  print("You lost")