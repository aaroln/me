# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the setly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import json
import os
import random
import string
import time
import requests
from typing import Dict, List


def give_me_five() -> int:
    """Returns the integer five."""
    i = 5
    return i


def password_please() -> str:
    """Returns a string, 8 or more characters long, contains at
    least one upper case letter and one lowercase letter.
    TIP: don't put in a real password!"""
    pw = 'Grasshopper'
    return pw


def list_please() -> list:
    """Returns a list, you can put anything in the list."""
    lst = [1,2,3]
    return lst


def int_list_please() -> list:
    """Returns a list of integers, any integers are fine."""
    lst_int = [1,2,3]
    return lst_int


def string_list_please() -> list:
    """Returns a list of strings, any string are fine."""
    lst_str = ['hello', 'ciao']
    return lst_str


def dictionary_please() -> dict:
    """Returns a dictionary, anything you like."""
    ry = {1: 'yellow'}
    return ry


def is_it_5(some_number) -> bool:
    """Returns True if the argument passed is 5, otherwise returns False."""
    if some_number == 5:
        well_is_it = True
    else:
        well_is_it = False
    return well_is_it


def take_five(some_number) -> int:
    """Subtracts 5 from some_number."""
    y = some_number - 5
    return y


def greet(name="Towering Timmy") -> str:
    """Return a greeting.
    return a string of "Well hello, " and the name argument.
    E.g. if given as "Towering Timmy" it should
         return "Well hello, Towering Timmy"
    """
    return f"Well hello, {name}"


def one_counter(input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of 1s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 2
    """
    count = 0

    for i in input_list:
        if i == 1:
            count += 1

    return count


def n_counter(search_for_this, input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    count = 0

    for i in input_list:
        if i == search_for_this:
            count += 1

    return count


def fizz_buzz() -> List:
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."

    from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special,
    and a string if it is. E.g.
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14,
         'FizzBuzz', 16, 17, ...]
    """
    fizz_buzz_list = []
    # your code here

    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            i = 'FizzBuzz'
            fizz_buzz_list.append(i)
        elif i % 3 == 0:
            i = 'Fizz'
            fizz_buzz_list.append(i)
        elif i % 5 == 0:
            i = 'Buzz'
            fizz_buzz_list.append(i)
        else:
            fizz_buzz_list.append(i)

    return fizz_buzz_list


def set_it_on_fire(input_string="very naughty boy") -> str:
    """Interleave the input_string with the 🔥 emoji.

    Given any string, interleave it with 🔥. Also make it be upper case.
    e.g. "very naughty boy" should return the string
    "🔥V🔥E🔥R🔥Y🔥 🔥N🔥A🔥U🔥G🔥H🔥T🔥Y🔥 🔥B🔥O🔥Y🔥"
    TIP: strings are pretty much lists of chars.
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a 🔥 on both ends of the string.
    """
    input_string = input_string.upper()
    lst = list(input_string)
    ls = []
    for i in lst:
        i = f"🔥{i}"
        ls.append(i)
    ls.append('🔥')

    st = "".join(ls)


    return st


def pet_filter(letter="a") -> List:
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
        "dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken", 
        "guinea pig", "donkey", "duck", "water buffalo", "python", "scorpion",
        "western honey bee", "dromedary camel", "horse", "silkmoth", 
        "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca", 
        "guineafowl", "ferret", "muscovy duck", "barbary dove", "cichlid",
        "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi", 
        "canary", "society finch", "fancy mouse", "siamese fighting fish", 
        "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"
    ]
    # fmt: on
    filtered = []

    for i in range(len(pets)):
        if letter in pets[i]:
            filtered.append(pets[i])

    return filtered


def best_letter_for_pets() -> str:
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    TIP: use the function you just wrote to help you here!
    TIP: you've seen this before in the pokedex.
    """
    import string

    the_alphabet = string.ascii_lowercase
    most_popular_letter = '0'
    mx = 0


    for i in the_alphabet:
        j = pet_filter(i)
        if len(j) > mx:
            mx = len(j)
            most_popular_letter = str(i)

    return most_popular_letter


def make_filler_text_dictionary() -> Dict:
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4
    If we set wordlength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    {
        3: ['Seb', 'the', 'yob', "boy"],
        4: ['aaaa', 'bbbb', 'cccc', "ddd"],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc', 'ddddddd']
    }
    Use the API to get the 4 words.

    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 4 words for each)
    TIP: you'll need the requests library
    """

    wd = {}
    lst = []
    for i in range(3,8):
        for j in range(4):
            url = f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={i}"
            r = requests.get(url)
            txt = r.text
            lst.append(txt)
        wd[i] = lst
        lst = []

    return wd


def random_filler_text(number_of_words=200) -> str:
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library,
        e.g. random.randint(low, high)
    """

    my_dict = make_filler_text_dictionary()

    words = []
    for i in range(number_of_words):
        length = random.randint(3, 7)
        wordchoice = random.randint(0, 3)
        words.append(my_dict[length][wordchoice])
    return " ".join(words)


def fast_filler(number_of_words=10) -> str:
    """Makes filler text, but really fast.

    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_cache.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the
    dictionary into and out of the file. Be careful when you read it back in,
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """

    """
    fname = "dict_cache.json"

    file_exists = os.path.exists(fname)
    if file_exists == False:
        dictionary = make_filler_text_dictionary()
        with open(fname, 'w', encoding='utf=8') as w:
            json.dump(dictionary, w)

    with open(fname, 'r', encoding='utf-8') as r:
        load = json.load(r)

    load = dict(load)

    c = dict((int(key), value) for (key, value) in load.items())

    words = []
    for i in range(number_of_words):
        length = random.randint(3, 7)
        wordchoice = random.randint(0, 3)
        words.append(c[length][wordchoice])
    x = " ".join(words)

    y = x.capitalize()

    y = y + "."

    return y

#fast_filler: Yodled yquem yodel yodel yolkier yuapin iurant waac icons gab.
#0 Uang iurant gab iurant yclad waac gab yont yont yodled gab yont uang yrbk fab gab waac icons gab aaronic.

#1 Aaronic aaronic yuapin ise gab uang gab yrbk ise iotize iurant yuapin uang yolkier waac yodel fab iotize fab yodel.

#2 Iurant ise yrbk fab gabarit ise yclad yolkier gabarit fab yodel wabbled yolkier yrbk wabbled yodel gabarit iotize ise waac.

#3 Yclad yrbk fab taa yquem yclad wabbled yodel aaronic aaronic gab yrbk aaronic yrbk yquem yodled yodel gabarit iotize iotize.
""" 

if __name__ == "__main__":
    print("give_me_five", give_me_five(), type(give_me_five()))
    print(
        "strong_password_please",
        password_please(),
        type(password_please()) == str,
    )
    print("int_list_please", int_list_please(), type(int_list_please()) == list)
    print(
        "string_list_please", string_list_please(), type(string_list_please()) == list
    )
    #print("dictionary_please", type(dictionary_please()) == dict)
    #print("is_it_5", is_it_5(5))
    #print("is_it_5", is_it_5(6))
    #print("take_five", take_five(5))
    #print("take_five", take_five(3))
    #print("greet:", greet())
    #print("three_counter:", one_counter())
    #print("n_counter:", n_counter(7))
    #print("fizz_buzz:", fizz_buzz())
    #print("put_behind_bars:", set_it_on_fire())
    #print("pet_filter:", pet_filter())
    #print("best_letter_for_pets:", best_letter_for_pets())
    #print("make_filler_text_dictionary:", make_filler_text_dictionary())
    #print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(4):
        print(i, fast_filler(number_of_words=20), "\n")
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
