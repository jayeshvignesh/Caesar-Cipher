from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)


def caesar(choice_of_crypting, text, shift_amount):
  if choice_of_crypting == "encode":
    encrypted_word = []
    for position in range(len(text)):
      letter_shifting = text[position]
      if letter_shifting.isalpha() == False:
        encrypted_word.append(letter_shifting)
      else:
        letter_position = int(alphabet.index(letter_shifting))
        encrypted_letter_position = letter_position + shift_amount
        if encrypted_letter_position > 25:
          encrypted_letter_position %= 26
        letter = alphabet[encrypted_letter_position]
        encrypted_word.append(letter)
    print(f"The encoded text is: \n{''.join(encrypted_word)}")
  elif choice_of_crypting == "decode":
    decrypted_word = []
    for position in range(len(text)):
      encrypted_letter = text[position]
      if encrypted_letter.isalpha() == False:
        decrypted_word.append(encrypted_letter)
      else:
        decrypted_letter_position = int(alphabet.index(encrypted_letter))
        letter_position = decrypted_letter_position - shift_amount
        if letter_position < 0:
          letter_position %= 26
        decrypted_letter = alphabet[letter_position]
        decrypted_word.append(decrypted_letter)
    print(f"The decoded text is: \n{''.join(decrypted_word)}")


go_again = "yes"
while go_again == "yes":
  direction = input(
      "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
  if direction != "encode" and direction != "decode":
    while direction != "encode" and direction != "decode":
      direction = input(
          "The answer you have entered is invalid. Please retype your decision for the following:\nType 'encode' to encrypt, type 'decode' to decrypt:\n"
      )
  text = input("Type your message:\n").lower().strip()
  shift = input("Type the shift number:\n")
  if shift.isdigit():
    shift = int(shift)
  else:
    while shift.isdigit() == False:
      shift = input(
          "The answer you have entered is invalid, \nso please retype the shift number:\n"
      )
    shift = int(shift)
  caesar(shift_amount=shift, choice_of_crypting=direction, text=text)
  go_again = input(
      "\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower().strip()

  if go_again != "yes" and go_again != "no":
    while go_again != "yes" and go_again != "no":
      go_again = input(
          "The answer you have entered is invalid. Please retype your decision for the following:\Type 'yes' if you want to go again. Otherwise type 'no'.\n"
      )

print("\nThank You for Using the Caesar Cipher.")
