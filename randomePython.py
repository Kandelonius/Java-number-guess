# This is a guesses the number game.

import random, math

print("Hello what is your name?")
name = input()

print("Well, "+ name +" I am thinking of a number between 1 and a number of your choosing")
print("Choose the max possible number'")
numberMax = int(input())

#print('DEBUG: secret number is ' + str(secretNumber))
def numberGuesser(num):
    secretNumber = random.randint(1, num)
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
        print('Congratulations '+ name +' you got it in ' + str(guessesTaken) + ' guesses')
    else:
        print('Nope the number I was thinking was ' + str(secretNumber))
print("I'm sure that's a fantastic number")
maxAttempts = math.ceil(math.log(numberMax, 2))
print("Technically it should only take you at most "+ str(maxAttempts) +" to figure out the random number I come up with when given "+ str(numberMax))
print("Although I don't envy your task if you choose to take on that endeavor")
numberGuesser(numberMax)


#import math /// math.log(a,Base)
