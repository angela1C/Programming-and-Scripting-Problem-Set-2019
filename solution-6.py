"""
# Solution to Problem 6 on the Problem Set 2019
# Angela Carpenter
# 23 March 2019

This program asks the user input a string and it will output every second word.
It takes a string input by the user, then splits the string into words. (A word is one or more characters separated by a space)
Go through the list of words but only print every second one.

My references for working on this problem are as follows:
[Section 3.1.2 of The Python Tutorial](https://docs.python.org/3/tutorial/introduction.html#strings)
[The section on String Methods in the Python Standard Library](https://docs.python.org/3/library/stdtypes.html#string-methods)
In particular:
[str.split()](https://docs.python.org/3/library/stdtypes.html#str.split) and [str.join](https://docs.python.org/3/library/stdtypes.html#str.join)
"""
# Ask the user to type in a sentence. The `str()` function converts the input of whatever characters into a string.
#This will be assigned to the variable 'sentence'. 
sentence = str(input("Please enter a sentence: "))

# using `.split()` string method to split the sentence into a list of words using the default of white space as the delimiter. Assign to words
words = sentence.split()  
# Count how many words in the sentence using `len()` function. Assign it to the variable num_words
num_words = len(words)  

# Using indexing to go through each word in the list `words` starting from the very first word, ending at the very last word, using a step size of 2 
# to  get every second word and assign them to other_word
other_word = words[::2] 
# Print the string formed by using the `str.join()` method to concatenate every second word in other_word with whitespace. 
print (" ".join(other_word))  

