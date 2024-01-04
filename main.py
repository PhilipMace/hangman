import random
import unicodedata


# Load the dictionary
with open('dictionary.txt', 'r') as f:  # Reads all the lines
    words = f.read().splitlines()


def get_word():
    word = strip_accents(random.choice(words)).upper()  # Makes all upper case

    return word

def strip_accents(word: str):
    """
    Strip accents from a given string.

    :param word: The string to strip accents from.
    :return: The string without any accents.

    Example:
    >>> strip_accents("é")
    'e'
    >>> strip_accents("ç")
    'c'
    >>> strip_accents("ñ")
    'n'

    """
    return ''.join(c for c in unicodedata.normalize('NFD', word)
                   if unicodedata.category(c) != 'Mn')

def display_word(word, guesses):
    return ' '.join(
        [letter if (i == 0 or i == len(word) - 1 or letter in guesses) else '_' for i, letter in enumerate(word)])


def hangman():
    print("Welcome to Hangman!")
    print("1: Single Player Mode")  # Game modes
    print("2: Two Player Mode")
    mode = input("Choose a mode (1 or 2): ")

    max_errors = 6  # Easily Modifiable

    if mode == '1':
        word = get_word()
    elif mode == '2':
        word = input("Player 1, enter a word: ").upper()
        print("\n" * 50)  # Clear the screen
    else:
        print("Invalid mode. Exiting game.")
        return

    guesses = set()
    if ' ' in word:
        guesses.add(' ')
    if '-' in word:
        guesses.add('-')
    errors = 0

    print(display_word(word, guesses))

    while errors < max_errors:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():  # Checks that they are all characters and not numbers or characters
            print("Please enter a single letter.")
            continue

        if guess in guesses:
            print("You already guessed that letter.")
        elif guess in word:
            guesses.add(guess)
            print("Good guess!")
        else:
            errors += 1
            print(f"Wrong guess. You have {max_errors - errors} attempts left.")

        print(display_word(word, guesses))

        if set(word) - set(' -') == guesses:
            print("Congratulations, you won!")
            return

    print(f"Game over. The word was {word}. You made {errors} errors.")


hangman()
