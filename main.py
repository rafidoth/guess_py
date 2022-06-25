import random


def guess(x) :
    random_number = random.randint(1, x)
    guess = -1
    guess_counter = 0
    while guess != random_number :
        guess = int(input(f"guess a number between 1 and {x} \n"))
        if guess > random_number :
            print("too high. Guess Again")
        elif guess < random_number :
            print("too low. Guess Again")
        else : print("You've guessed the correct number")
        guess_counter = guess_counter+1
        if guess_counter == 5 :
            print("GAME OVER")
            print(f"The number was {random_number}")
            break

guess(50)
