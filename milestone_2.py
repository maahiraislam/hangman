import random

word_list = ["Strawberries","Raspberries","Apples","Oranges","Mangoes"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1:
    print("Good guess!")
else:
    print("OOps! That is not a valid input.")