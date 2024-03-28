# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math
from re import M


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0

    while True:

        guess = high - ((high - low) // 2)
        results = {"guess": guess, "tries": tries}

        tries += 1

        if guess == actual_number:
            return results
        elif guess < actual_number:
            low = guess + 1
            print(results)
        else:
            high = guess - 1
            print(results)

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print("\n")
    print(binary_search(1, 100, 6))
    print("\n")
    print(binary_search(1, 100, 95))
    print("\n")
    print(binary_search(1, 51, 5))
    print("\n")
    print(binary_search(1, 50, 5))
