"""
# Solution to Problem 4 on the Problem Set 2019
# Angela Carpenter
# 24 March 2019

This program asks the user to input a positive integer as x. It outputs a sequence of numbers starting with that number x as the first term. 
The rest of the terms in the sequence are calculated from the previous terms by halving the previous term if it was even 
or by multiplying the previous term by 3 and adding 1 to this product if the previous term was odd. The last number in the sequence is 1.

This code relates to the Collatz Conjecture. For some basic information on this refer to wikipedia at https://en.wikipedia.org/wiki/Collatz_conjecture
The Examples section on the wikipedia page provided some examples showing the seqeunces that should be generated for a particular number.
I used this to test my code.

My references for working on this problem are as follows:
Wikipedia at https://en.wikipedia.org/wiki/Collatz_conjecture
Python Tutorial  - Section 8.3 Handling Exceptions of the Python tutorial. I used this for the input part of the program.
Python Tutorial  - section on using while loops and also the section on break statements
https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

"""
# This part of the code asks the user to input a valid positive integer. 
# If the input is not a positive integer then the user will be asked again and again until a valid positive integer is entered.
while True:
    ## while True, executed  the `try` statements. If the input is valid, the `break` statement terminates this `while` loop (skipping `except`)
    try:
        ## ask the user to enter a positive integer and assign it to the variable x
        x = int(input("Please enter a positive integer: ")) 
        # Check if the input was a negative number and if this is true then a `ValueError` is raised. 
        if x < 0:
           raise ValueError
        break  
    except ValueError:
        # if there is a ValueError (either a non-integer or a negative integer) then print the following message
        print("That was not a positive integer. Please try again!")

## create num_terms variable to count the number of terms in the sequence. At each step increase its value by 1. can check the output against the Wikipedia page
num_terms = 1
# create a list to hold the sequence. x will be the only element to start
my_seq =[x]
## While x is greater than 1, execute the statements in this while loop
while  x > 1:
    # check if current value of x is even and if it is even, divide x by 2 and update x to be this value
    if x % 2 == 0:  
        x = x //2
        # append x to the my_seq list as the next term in the sequence (instead of printing the term)
        my_seq.append(x)
        ## increment the term counter variable by 1
        num_terms += 1
        
## however if the current value of x is odd, multiply x by 3 and then add 1 to this product. Update x to be this 
    else:
        x = (x * 3) + 1
        # print(x)
        # append x to the my_seq list as the next term in the sequence (instead of printing the term)
        my_seq.append(x)
        # increment the term counter variable by 1
        num_terms +=1
      
#print("The number of terms in the sequence is ",num_terms)

print(*my_seq, sep = ", ")
# as per stackoverflow post (https://stackoverflow.com/a/35119046) the star * unpacks the list 
# and returns every element in the list without the brackets
 
