#Introduction and rules
print("Welcome to the guessing game. The game will generate a random number between 1 to 100. See how many tries you will take to guess the random number.")
print("If you are within 10 of the random number in your first try, the game will say 'Warm', else it will say 'Cold'")
print("On all subsequent turns, it will say 'Warmer' if you are getting closer or 'Colder' if you are getting farther from the number")

# Import Random library and randint function. 
#Generate random number between 1 to 100 and assign to variable a
from random import randint
a = randint(1,100)

#Ask for first user input. 
#Set a variable for guess counter (c) and set it to 1
i = int(input ("Enter a number between 1 to 100"))
c = 1

#While guess is not equal to random number
while i!=a:
#For first guess
#If guess is out of bounds, guess is invalid and not counted
#Create a variable x to measure absolute difference between guess and answer. Do this for all valid guesses
    if c<=1:
        if i<1 or i>100:
            print("Invalid Guess. Enter a number between 1 to 100")
            i = int(input("Try Again. Enter a number between 1 to 100"))
        elif i<(a+10)and i>(a-10):
            print("Warm")
            c= c+1
            x=abs(a-i)
            i=int(input("Try again. Enter a number"))
        elif i>(a+10) or i<(a-10):
            print("Cold")
            c = c+1
            x=abs(a-i)
            i=int(input("Try again. Enter a number"))
# For all subsequent guesses        
# Again invalid guesses (out of bounds) are not counted
# Warmer or hotter is done by comparing stored value of absolute difference x to current difference
    elif c>1:
        if i<1 or i>100:
            print("Invalid Guess. Enter a number between 1 to 100")
            i = int(input("Try Again. Enter a number between 1 to 100"))
        elif abs(a-i)<=x:
            print("Warmer")
            c=c+1
            x=abs(a-i)
            i=int(input("Try again. Enter a number"))
        elif abs(a-i)>x:
            print("Colder")
            c=c+1
            x=abs(a-i)
            i=int(input("Try again. Enter a number"))
# when guess is equal to random number
# Print out feedback along with number of guesses
else:
    print('Correct answer!!!. Number of guesses needed was {}'.format(c))
