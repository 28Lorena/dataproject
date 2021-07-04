import random

number = random.randint(1,10)

guess = int(input ("Guess a number between 1 and 10: "))

while guess != number:
    if guess < number:
        print ("You need to guess higher. Try again")
        guess = int(input ("Guess a number between 1 and 10: "))
    else:
        print ("You need to guess lower. Try again")
        guess = int(input ("Guess a number between 1 and 10: "))

print ("You guessed the number correctly1")
