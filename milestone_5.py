import random
word_list = ["Strawberries","Raspberries","Apples","Oranges","Mangoes"]
class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self,guess):
        lowercase_word = self.word.lower()
        guess_letter = guess.lower()
        if guess_letter in lowercase_word:
            print(f"Good guess! {guess_letter} is in the word.")
            for char, letter in enumerate(lowercase_word):
                if guess_letter == letter:
                    self.word_guessed[char] = guess_letter
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess_letter} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
        


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    print(game.word)
    while True:
        if game.num_lives == 0:
            print("The game has ended, you have lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif num_lives > 0 and game.num_letters == 0: 
            print("Congratulations. You won the game!")
            break
    

play_game(word_list)