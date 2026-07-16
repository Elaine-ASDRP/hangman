# This is the Hangman python script
from english_words import get_english_words_set
import random


def initialize_word_bank():
    """Return a list of English words between 4 and 12 letters."""
    words_set = get_english_words_set(["web2"], lower=True)
    return [word for word in words_set if 4 <= len(word) <= 12]


# Use a set for faster lookups
alphabet = set("abcdefghijklmnopqrstuvwxyz")


def display_word(secret_word, guessed_letters):
    """Return the current state of the word with blanks."""
    return " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )


def check_guess(secret_word, guessed_letters, lives):
    """Get a valid guess from the user and update lives."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        # Must be exactly one character
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        # Must be a letter
        if guess not in alphabet:
            print("Please enter a valid letter.")
            continue

        # Cannot guess the same letter twice
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            print("Letter not found!")
            lives -= 1

        return lives


def play_single_game(word_list):
    """Play one round of Hangman."""
    secret_word = random.choice(word_list)
    guessed_letters = []
    lives = 6

    print("Let's play Hangman!")

    while lives > 0:
        print("Word:", display_word(secret_word, guessed_letters))
        print(f"Lives remaining: {lives}")
        print("Guessed letters:", " ".join(guessed_letters))

        lives = check_guess(secret_word, guessed_letters, lives)

        # Check if the player has guessed every letter
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word!")
            print(f"The word was: {secret_word}")
            return

    print("Game over!")
    print(f"The word was: {secret_word}")


def main():
    """Main game loop."""
    word_list = initialize_word_bank()

    while True:
        play_single_game(word_list)

        response = input("\nPlay again? (y/n): ").strip().lower()

        if response == "y":
            print("Starting a new game...")
        elif response == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Exiting game.")
            break


if __name__ == "__main__":
    main()

