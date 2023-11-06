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
    guesses = guess.lower()
    if guesses in word:
        print(f"Good guess! {guesses} is in the word.")
    else:
        print(f"Sorry, {guesses} is not in the word. Try again.") 

ask_for_input()