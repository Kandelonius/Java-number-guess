# This is a guess the number game.

import random

print("Hello what is your name?")
name = input()

print("Well, " + ", I am thinking of a number between 1 and 20")

secretNumber = random.randint(1, 20)

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    if(guess < secretNumber):
        print('Your guess is too low')
    elif(guess > secretNumber):
        print('Your guess is too high')
    else:
        break #the condition was satisfied

if(guess == secretNumber):
    print('Congratulations you got it in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope the nmber I was thinking was ' + str(secretNumber))
