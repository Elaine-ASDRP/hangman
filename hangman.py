# This is the Hangman python script
from english_words import get_english_words_set
import random 

def initialize_word_bank(): 
    """Initialize, return a set of English words from the web2 word list

    Returns:
        list: complete list of words between [4, 12] characters long
    """
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


print(" ".join(display = ["_"] * len(secret_word)))

def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )
    
def check_guess(secret_word, alphabet, guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        print(f"Lives left: {lives}")
        if lives == 0:
        print(f"Out of lives! The word was '{secret_word}'.")
        break

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

def main():
    """Control overall game loop and execute hangman game logic
    """
    word_list = initialize_word_bank()

    play_again = True 

    while play_again is True: 
        play_single_game(word_list) 

        while True: 
            print("Play again? [y/n]")
            response = input(">").lowercase().strip()

            if response =="y": 
                print("New game")
                play_again = True
                break 
            elif response == "n":
                print("Thanks for playing")
                play_again = False
                break 
            else: 
                print("Invalid input. Play again? [y/n]")

