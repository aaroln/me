"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random
from tempfile import TemporaryFile


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("This is a guessing game!")

    lower_bound = get_number("Enter a lower bound: ")

    while True:
        upper_bound = get_number("Enter an upper bound: ")

        if lower_bound < upper_bound:
            print(f"Your lower bound is {lower_bound} and your upper bound is {upper_bound}")
            break
        else:
            print("That number is not greater than your lower bound!")
            continue
        
    random_number = random.randint(lower_bound, upper_bound)

    print("Go on, have a guess!")

    while True:
        guess = get_number(f"Enter a number between {lower_bound} and {upper_bound}: ")

        if lower_bound < guess < upper_bound:
            if guess == random_number:
              print(f"You got it! The number was {guess}")
              return "You da boss"
            elif guess > random_number:
                print(f"Try less than that!")
            else: 
                print("Try more than that!")
        else:
            print(f"That number is not between {lower_bound} and {upper_bound}")


              
def get_number(sentence):
    while True:
        value = input(sentence)

        try:
            value = int(value)
            return value

        except ValueError:
            print("That's not a number!")
            continue


if __name__ == "__main__":
    print(advancedGuessingGame())
