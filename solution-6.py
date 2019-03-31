# solution-6.py
# This is my solution to Problem 6 on the Problem Set 2019.
# Angela Carpenter
# 31st March 2019

# Ask the user to type in a sentence. The str() function converts the input of whatever characters into a string.
# This will be assigned to the variable 'sentence'. 
sentence = str(input("Please enter a sentence: "))

# using .split() string method to split the sentence into a list of words using the default of white space as the delimiter.
words = sentence.split()  
# Count how many words in the sentence using len() function. 
num_words = len(words)  

# Using indexing to go through each word in the list of words starting from the very first word, ending at the very last word,
# using a step size of 2 to  get every second word
other_word = words[::2] 
# Print the string formed by using the `str.join()` method to concatenate every second word in other_word with whitespace. 
print (" ".join(other_word))  

