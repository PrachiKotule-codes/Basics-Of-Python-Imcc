#program to number number between 1-9 
import random
target = random.randint (1, 9)
guess = int(input ("Guess a number between 1 and 9: "))
if guess == target:
    print ("You won 100 points!")
else:
    print("Try again")

