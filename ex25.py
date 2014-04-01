def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
# wyss running through python manually:
# 
# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> 
# >>> 
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> wrods
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'wrods' is not defined
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
# 
#
# typing in help(ex25) shows the documentation comments as shown below
# 
# Help on module ex25:
# 
# NAME
#     ex25
# 
# FILE
#     /Users/cory/git/python_the_hard_way/ex25.py
# 
# FUNCTIONS
#     break_words(stuff)
#         This function will break up words for us.
#     
#     print_first_and_last(sentence)
#         Prints the first and last words of the sentence.
#     
#     print_first_and_last_sorted(sentence)
#         Sorts the words then prints the first and last one.
#     
#     print_first_word(words)
#         Prints the first word after popping it off.
#     
#     print_last_word(words)
#         Prints the last word after popping it off.
#     
#     sort_sentence(sentence)
#         Takes in a full sentence and returns the sorted words.
#     
#     sort_words(words)
#         Sorts the words.
# 
# (END) 
# 
# 
# import everything from ex25 by doing the following. this way
# we don't have to type in ex25 every time to call the functions
# 
# >>> from ex25 import *
# >>> sentence = "These are all good things I think."
# >>> words = break_words(sentence)
# >>> words
# ['These', 'are', 'all', 'good', 'things', 'I', 'think.']
# >>> 
# 
# 
# after breaking the program
# 
# >>> sentence = "A test sentence that will break."
# >>> words = break_words(sentence)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "ex25.py", line 3, in break_words
#     words = stuff.splift(' ')
# AttributeError: 'str' object has no attribute 'splift'
# >>> 
# 
# 
# pop words test. keep in mind 0 is the first, using a minus - tells it
# to go left (reverse order) as shown below
# 
# >>> from ex25 import *
# >>> sentence = "This is a test sentence to run functions against."
# >>> words = break_words(sentence)
# >>> words
# ['This', 'is', 'a', 'test', 'sentence', 'to', 'run', 'functions', 'against.']
# >>> 
# >>> print_first_word(words)
# a
# >>> print_last_word(words)
# functions
# >>> 
# 
#