"""
This program asks the user input a string and it will output every second word.

This program contains my code for the sixth problem on the Problem Set 2019:
Write a program that takes a user input string and outputs every second word.
$ python secondstring.py

Example of running the program
Please enter a sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog
---------------------------------------

Take a string input by the user.
Split the string into words. 
A word is one or more characters separated by a space.
Go through the list of words but only print every second one.

My sources for working on this problem are as follows:
[Section 3.1.2 of The Python Tutorial](https://docs.python.org/3/tutorial/introduction.html#strings)

[The section on String Methods in the Python Standard Library](https://docs.python.org/3/library/stdtypes.html#string-methods)
In particular:
[str.split()](https://docs.python.org/3/library/stdtypes.html#str.split) and [str.join](https://docs.python.org/3/library/stdtypes.html#str.join)
"""
# This code asks a user to type in a sentence. The `str()` function converts the input into a string.
# This will be assigned to the variable 'sentence'. 

sentence= str(input("Please enter a sentence: "))

# using the .split() string method to split the sentence into words using the default white space as the delimiter.
# assign the output to words. `str.split()` returns a list
words = sentence.split()  
# Count how many words in the sentence using `len()` function. Assign it to the variable num_words
num_words = len(words)  

"""
# Using a for loop to iterate over the indices of each word in the sentence using the `range()` and `len()` function combined
# Range from zero up the number of words in the sentence, in steps of 2 to get the index for every second word.
# This prints every second word but it puts them on a separate line instead of beside each other.

for i in range(0,len(words),2):
    print(words[i])  
 """  
# Here I am using indexing to go through each word in words starting from the first word, ending at the last word, using a step size of 2 
# to  get every second word and assign them to other_word
other_word = words[::2] 
# Print the string formed by using the `str.join()` method to concatenate every second word in other_word with whitespace. 
print (" ".join(other_word))  

