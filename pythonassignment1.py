import random
import math
#generating random number between 1 and 10
x = random.randint(1, 10)
print("\n\tYou have only 5 chances to guess the integer!\n")
print("I've already guessed one.")


#initializing the number of guesses
count = 0
#for calculation of minimium number of guesses depends upon range
while count < 5:
    count +=1
    #taking guesses number as input
    guess = int(input("Enter you guess: "))

    #condition testing
    if x == guess:
        print("Its a match! Congratulations. Play again.")
        break
    if math.fabs(x - guess) < 9 or math.fabs(x - guess) < 8:
        print("You guess is very cold. Try again")
    elif math.fabs(x - guess) < 7 or math.fabs(x - guess) < 6:
        print("You guess is cold. Try again")
    elif math.fabs(x - guess) < 5 or math.fabs(x - guess) < 4:
        print("You guess is neutral. Try again")
    elif math.fabs(x - guess) < 3:
        print("You guess is warm. Try again")
    elif math.fabs(x - guess) < 2:
        print("You guess is hot. Try again")
        break
    
    if count >= 5:
#if guessing is more than required guesses
        print("\nThe number is %d" % x)
        print("\tBetter luck next time!")

