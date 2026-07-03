# This is the Hangman python script
from english_words import get_english_words_set
import random 

def initialize_word_bank(): 
    words_set = get_english_words_set(['web2'], lower=True)
    # optional: filter words to keep them b/w 4-12 letters 
    word_list = [word for word in words_set if 4 <= length(word) <= 12]
    return list(word_list)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("Let's play hangman!")
