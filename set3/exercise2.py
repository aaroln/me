"""Set 3, Exercise 2.

An example of how a guessing game might be written.
Play it through a few times, but also stress test it. What if your lower bound 
is 🍟, or your guess is "pencil", or "seven"
This will give you some intuition about how to make exercise 3 more robust.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")

    while True:

        upper_bound = input("Enter your upper bound: ")

        try:
            upper_bound = int(upper_bound)
            print(f"You entered {upper_bound} as your upper_bound.")
            break

        except ValueError:
            print("That's not a number!")
            continue

    random_number = random.randint(0, upper_bound)

    print(random_number)

    print("Go on, have a guess!")

    while True:

        guess = input(f"Enter a number between 0 and {upper_bound}: ")

        try:
            guess = int(guess)

            if 0 < guess < upper_bound:

                if guess == random_number:
                    print(f"You got it! The number was {random_number}.")
                    return guess
                elif guess > random_number:
                    print(f"Try less than that!")
                else:
                    print("Try more than that!")
            else:
                print(f"That number isn't between 0 and {upper_bound}!")

        except ValueError:
            print("That's not a number!")
            continue

if __name__ == "__main__":
    exampleGuessingGame()
