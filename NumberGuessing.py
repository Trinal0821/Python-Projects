import random

for x in range(1):
    number = random.randint(1, 101)


print("Welcome to Number game!")
print()
print("In this game, you will guess a number from 1 to 100. If you guess the number")
print("correctly, then you will win! Along the way, there will be some helpful hints")
print("that tells you whether you're above or below that number.")
print()
print("Now lets get started!")
print()
print("Would you like some hints during the game? (Y/N)")
choice = input()
yes = 'Y'
no = 'N'

print("What do you think the number is?")
userGuess = int(input())
count = 0

if choice == yes:
    while(userGuess != number):
        if userGuess > number:
            print("The number you have chosen is greater than the number. Try again.")
            print()
            count = count + 1
            print("What do you think the number is?")
            userGuess = int(input())


        else:
            print("The number you have chosen is less than the number. Try again.")
            print()
            count = count + 1
            print("What do you think the number is?")
            userGuess = int(input())

else:
    while (userGuess != number):
        if userGuess > number:
            print("Try again.")
            print()
            count = count + 1
            print("What do you think the number is?")
            userGuess = int(input())


        else:
            print("Try again.")
            print()
            count = count + 1
            print("What do you think the number is?")
            userGuess = int(input())



print("Congratulations! You go it right! It took you {} tries. Play again and try to beat your score!".format(count))


