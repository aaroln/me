"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# This will create a list called 'some_words'
some_words = ["what", "does", "this", "line", "do", "?"] #created a list 

# Select the first word in the list and then print it. This loop will continue until it has gone through all the strings in the list.
for word in some_words:
    print(word) # prints each string onto a separate line. 

# Will perform the same, however, it will be under a new variable 'x'.
for x in some_words:
    print(x) # Printed each word onto a separate line.

# This will print out the full list
print(some_words) # Printed out the list.

# If the length of the list 'some_words' is greater than 3, will print the string. if it's not, nothing will happen. 
if len(some_words) > 3:
    print("some_words contains more than 3 words")


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
