# Define a function called word_counter that accepts one string argument and returns a
# number representing how many separate words are in that string. For example:

def word_counter(word):
    return len(word.split())

print(word_counter("Hello world")) # returns 2

print(word_counter("This is a sentence")) # returns 4

print(word_counter("")) # returns 0
