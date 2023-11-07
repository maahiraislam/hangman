import random
word_list = ["Strawberries","Raspberries","Apples","Oranges","Mangoes"]
class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(self.word_guessed)
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess_letter = guess.lower()
        if guess_letter in self.word:
            print(f"Good guess! {guess_letter} is in the word.")
            for char in range(len(self.word)):
                letter = self.word[char]
                if letter == guess_letter:
                    self.word_guessed[char] = guess_letter
            self.num_lives -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess_letter} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        guess = input("Guess a letter: ")
        while True:
            if guess.isalpha() == False or  len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                guess = input("Guess a letter: ")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
my_Hangman = Hangman(word_list,num_lives=5)
my_Hangman.ask_for_input()

        