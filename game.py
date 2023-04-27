import random

number = random.randint(1, 100)
guess = None
guesses = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations, you guessed the number in {guesses} guesses!")
