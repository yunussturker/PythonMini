import random

entered = input("Type a number: ")

if entered.isdigit():
    entered = int(entered)

    if entered <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

randNum = random.randint(0, entered)
guess = 0

while True:
    guess += 1
    userGuess= input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number next time.")
        continue
    if userGuess == randNum:
        print("You got it!")
        break
    elif userGuess > randNum:
        print("You were above the number.")
    else:
        print("You were below the number.")

print("You got it in " + str(guess) + " guesses!")



