import random
from Hangman_Words import words
import string

def get_valid_word(word_list):
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        print("You have used these letters: ", " ".join(used_letters))
        word_guess_progress = [letter if letter in used_letters else "_" for letter in word]
        print("Your progress towards guessing the word: ", " ".join(word_guess_progress))
        user_guess = input("Guess a letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
        elif user_guess in used_letters:
            print("Invalid guess. You have already used that letter.")
        else:
            print("Invalid guess. You tried to guess an invalid letter.")
    print("The word was " + word + ".")

hangman()
print("You have finished the game.")