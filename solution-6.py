"""
Write a program that takes a user input string and outputs every second word.
$ python secondstring.py
Example of running the program
Please enter a sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog

This question is looking at string functions. 
For this question I am referring to the section on string methods on the python standard library at https://docs.python.org/3/library/stdtypes.html#string-methods 
It was also covered in week 7 of the course
str.split() function splits a string up into words. By default str.split splits on white space and returns a list.

`str.split(sep=None, maxsplit=-1)` will return a list of the words in the string, using sep as the delimiter string.`

The opposite to split is join. str.join returns a string back while split returns a list.
"""
## this program asks a user to type in a sentence. This will be assigned to the variable 'sentence'
sentence= str(input("Please enter a sentence: "))  ## asks the user to type in a sentence

words = sentence.split()  ## split the sentence into words using the default white space as the separator.

print(len(words))  ## can use len to count how many words in the sentence
num_words = len(words)  ## assign this to variable num_words
print("There are ",num_words, "words in that sentence")  ## just for now
for i in range(0,num_words,2):  ## using a for loop to go through each word starting at zero and using a step size of 2
    print(words[i])  ## print every second word 

"""
##This seems to be given the required output however it is printing each word to a new row on a separate line.
In week 7 we looked at slicing strings. The step argument can be specified
If I set it to 2 then it will take every second word.
However when it prints out it is including the square brackets of the list as str.split returns a list

The opposite to str.split is str.join.

From https://docs.python.org/3/library/stdtypes.html#lists section on String Methods
str.join str.join(iterable) Return a string which is the concatenation of the strings in iterable. 

""" 

print(words[::2])  ## this is printing every second word but as a list
other_word = words[::2]  ## assign to a variable other_word
print(type(other_word))  # this shows it is a list

print (" ".join(other_word))  ## now using str.join to join white space with every second word.
# str.join returns a string

