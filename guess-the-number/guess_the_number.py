import random

def generate_randnum():             # Generates a random number between 1 and 100
    return random.randint(1, 100)

def guessing():             # Takes input from the user
    while True:
        guess = input("Guess a number between 1 and 100: ")
        if guess.isdigit():
            return int(guess)
        print("Please enter a valid number")

def check_num(num):             # Checks how close or correct is the user
    while True:
        inp = guessing()
        if inp == num:              # correct guess
            print("Congrats! That's correct.")  
            break
        else:
            if inp < num:               # guess is low
                print("Too low")
            else:                       # guess is high
                print("Too high")

num = generate_randnum()
check_num(num)