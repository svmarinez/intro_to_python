"""
Number guessing game

You have 3 tries to guess a number between 1 and 20.
"""
import random


answer = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20")

guess = int(input("Make a guess: "))

if guess != answer:
    tries = []
    for i in range(2):
        if guess < answer:
            print("Too low.")
            tries.append(False)
        else:
            print("Too high.")
            tries.append(False)
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            break
    if tries == [False, False] and guess != answer:   
        print(f"You've used all your tries. The answer was {answer}.")

    