import random

word_list = ["Strawberries","Raspberries","Apples","Oranges","Mangoes"]
word = random.choice(word_list)



def ask_for_input():
    guess = input("Guess a letter: ")
    while True:
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            guess = input("Guess a letter: ")
    check(guess)

def check(guess):
    guess_letter = guess.lower()
    if guess_letter in word:
        print(f"Good guess! {guess_letter} is in the word.")
    else:
        print(f"Sorry, {guess_letter} is not in the word. Try again.") 

ask_for_input()