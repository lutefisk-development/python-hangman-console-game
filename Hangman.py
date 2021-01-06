

### Hangman - Console based game
import random

'''
FEATURES:

[x] En välkomsttext skrivs ut i konsolen.

[x] Ett hemligt ord slumpas fram (eller bestäms i förväg, spelar ingen roll egentligen) och detta ord skrivs ut i konsolen fast endast med understreck istället för de faktiska bokstäverna.

[x] Spelaren upmanas att gissa, en prompt dyker upp där spelaren kan skriva in sin gissning. OBS (följande är frivilligt men bra övning), någon form av felhantering bör finnas på denna gissning så att programmet försäkrar sig om att den endast får EN bokstav som gissning (inte flera) och att gissningen är just bokstäver och inga andra tecken.

[x] Spelarens gissning checkas emot tidigare gissade bokstäver (om det finns), är det så, så bör spelaren få gissa om. Om man har gjort felhanteringen från ovan så bör man även få gissa om, om man råkar skriva in en fel inmatning. En loop bör alltså omsluta hela gissningskoden.

[x] Gissar spelaren rätt så ska understrecket på motsvarande plats/er i den hemliga ordet bytas ut mot den gissade bokstaven. Skulle det vara så att man lyckades gissa rätt på den sista bokstaven så måste en check göras här för att se om man vunnit eller inte. I så fall ska en vinnande text skrivas ut och spelet avbrytas.

[x] Gissar spelaren fel så ska det skrivas ut i konsolen och någon form av räknare bör räknas ner. Hamnar man på noll så “hängs man” och spelet avslutas.

[x] Nu är en gissningsrunda avslutat, nu bör man fortsätta till den andra gissningsrundan, alltså det bör finnas en spelloop som pågår fram tills att det hemliga ordert har gissats fram.

[x] Funktioner som kallar på andra funktioner
'''

def get_secret_word():
  '''
  Get a random word from the secret words array
  '''

  secret_words = [
  'javascript',
  'python',
  'array',
  'loop',
  'function',
  'inheritance'
  ]

  return random.choice(secret_words)

def get_user_input():
  '''
  User guesses a letter for the Hangman game
  '''

  return input('\nGuess a letter: ')

def validation_rules():
  '''
  Validates only a single alpha character at lowercase
  '''

  guessed_letter = get_user_input()

  # Validates only one letter from user
  if len(guessed_letter) > 1:
    print('\nPick only one letter!')
    guessed_letter = get_user_input()

  # Validates only alpha characters (a-z or A-Z)
  if not guessed_letter.isalpha():
    print('\nThis is not a letter, try again.')
    guessed_letter = get_user_input()

  # Returns user input as lowercase
  return guessed_letter.lower()

def check_guessed_letter(secret_word, guessed_letter):
  '''
  Checks if the guessed letter is in the secret word\n
  Returns True or False
  '''
  if secret_word.count(guessed_letter) >= 1: return True
  else: return False

def validate_guessed_letter(previously_guessed_letters, guessed_letter):
  '''
  Checks if the guessed letter has been guessed before\n
  Returns a string of already guessed letters OR False
  '''

  # Checks if the guessed letter exists in the previously guessed letters string
  if previously_guessed_letters.find(guessed_letter) == -1:
    # If the letter has not been guessed before, add the letter to the string
    previously_guessed_letters = ''.join((previously_guessed_letters, guessed_letter))

    return previously_guessed_letters 
  else:
    return False

def run_game(): 
  '''
  Starts the Hangman game
  '''
  print('\nWelcome to the Hangman console game')

  # This is how many tries the user has before the game ends
  lives = 6

  # This is the currently secret word
  secret_word = get_secret_word()

  # This is the secret word with underscores
  current_word = '_' * len(secret_word)

  # Empty string of previously guessed letters
  previously_guessed_letters = ''

  # Starting text
  print(f'\nYou have {lives} lives, and the word is: ')

  # The loop that runs the game
  while lives > 0:
    print(f'\n{current_word}')

    # Get validated user input
    guessed_letter = validation_rules()
    
    # Validate that the user input has been guessed
    validation = validate_guessed_letter(previously_guessed_letters, guessed_letter)

    # Statement that checks if the secret word contains the guessed letter
    if check_guessed_letter(secret_word, guessed_letter):
      if validation != False:
        previously_guessed_letters = validation
        # IF this is true, add the letter to the correct place in the current_word variable

        # Get all matching indexes in the secret word
        matched_indexes = [i for i, letter in enumerate(secret_word) if letter == guessed_letter]

        # Loops through the array of indexes and switch out '_' for the guessed letter
        for index in matched_indexes:
          current_word = current_word[:index] + guessed_letter + current_word[index + 1:]
      else:
        # If the guessed letter has been guessed before, print a message to the user
        print('\nYou have already tried that letter, try again.')

    else:
      # IF this is false, subtract 1 life from the lives variable

      if validation != False:
        previously_guessed_letters = validation

        # Since the user guessed the wrong letter, remove one life, hence shortening the while loop
        lives -= 1

        # Once lives equals 0 the while loop ends, and the user looses the game
        if lives == 0:
          print('\nGame Over :(')
        else:
          # Prints a message to the user that he/she has guessed wrong and also how many lives/tries left
          print(f'\nSorry, that letter is not in the secret word, you have {lives} lives left')
      else:
        # If the guessed letter has been guessed before, print a message to the user
        print('\nYou have already tried that letter, try again.')
    
    # Winning the game
    if secret_word == current_word:
      print(f'\nYou win!! - the word was {secret_word}')
      break

run_game()
