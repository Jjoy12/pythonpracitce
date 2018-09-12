import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New Number: "))
    if guess > 0:
        print("Number is too large")
    elif guess < to_be_guessed:
            print("Number is too small")
    else:
        print("Sorry that youre giving up!")
        break
else:
    print("congradulations you made it")