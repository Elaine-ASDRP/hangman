# This is the Hangman python script
from english_words import get_english_words_set
import random 

def initialize_word_bank(): 
    words_set = get_english_words_set(['web2'], lower=True)
    # optional: filter words to keep them b/w 4-12 letters 
    word_list = [word for word in words_set if 4 <= len(word) <= 12]
    return list(word_list)


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("Let's play hangman!")

word_bank = initialize_word_bank()
secret_word = random.choice(word_bank)
#empty list, will grow to contain all the letters guessed, helps avoid repeats
guessed_letters = []
wrong_guesses = 0
#six lives
lives = 6 
guess= "ab"

def check_guess(secret_word, alphabet, guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()

        # Check that exactly one character was entered
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        # Check that it is a letter
        if guess not in alphabet:
            print("Please enter a valid letter.")
            continue

        # Check if it has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

