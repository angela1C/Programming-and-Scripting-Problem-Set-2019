"""
This program asks the user to input a positive integer. It outputs a sequence of numbers starting with that number as the first term. The rest of the terms are 
calculated from the previous terms by halving the previous term if it was even, or by multiplying the previous term by 3 and adding 1 to this product.
The last number in the sequence is 1.

This code relates to the Collatz Conjecture. For some basic information on this refer to wikipedia at https://en.wikipedia.org/wiki/Collatz_conjecture

This program contains my code for the fourth problem on the Problem Set 2019:
4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
At each step calculate the next value by taking the current value and,if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
Have the program end if the current value is one.

example given of running the program:
$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1

----------
The programs asks the user to input a positive integer X. This will be the first term in the sequence
The program then does some calculation on the number based on an if-elif statements to calculate the next term

If the current value of x is even (if x % 2 is 0), then divide x by 2. Update the value of x to be this number. Print this number
If the current value of x is odd (if x % 2 is 1), then multiply x by 3 and add 1 to the product. Update the value of x to be this number. Print this number
If the current value of x is 1 then the program should end. 
The program should result in a sequence beginning with x and ending with 1.


The section on Examples on the wikipedia page provided some examples showing the seqeunces that should be generated for a particular number.
I used this to test my code.

My sources for working on this problem are as follows:

Wikipedia at https://en.wikipedia.org/wiki/Collatz_conjecture
Python Tutorial  - Section 8.3 Handling Exceptions of the Python tutorial. I used this for the input part of the program.


Python Tutorial  - section on using while loops and also the section on break statements
https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops


"""
## This part of the code asks the user to input a valid positive integer. 
# If the input is not a positive integer then the user will be asked again and again until a valid positive integer is entered.
while True:
    ## while True, the statements between `try` and `except` are executed and the value of x will be printed
    # If the input by the user is valid, then the `break` statement terminates this `while` loop. The `except` clause of `try` is then skipped.
    try:
        ## ask the user to enter a positive integer and assign it to the variable x
        x = int(input("Please enter a positive integer: ")) 
        ## The `int()` function accepts both positive and negative integers. However only positive integers are valid inputs for this program
        # Using `if` statement to check if the input was a negative number and if this is true then a `ValueError` is raised. 
        # a ValueError is where the argument received is of the right type, in this case an integer but with an inappropriate value, ie less than 0
        if x < 0:
           raise ValueError
        break  
    except ValueError:
        # if there is a ValueError (either a non-integer or a negative integer) then print the following message
        print("That was not a valid positive integer. Please enter a positive integer")

    # the error message will keep printing until a valid integer is entered. Ctrl + C will terminate the process using a keyboard interrupt.
    # Maybe I should enclose this section in a for loop so it doesn't go on forever...

## Once a valid integer has been entered, print x. This will be the first term in the sequence.
print(x)

"""
I did use a for loop initially for this, however on testing my code I can see the for loop will not work for all numbers and did not get to 1.
A for loop will only generate x number of terms, however for some numbers the number of terms in the sequence will exceed x.
A while loop makes more sense as it keeps going until a condition evaluates to false.
As an aside this made me think how many terms are generated for the diffent numbers so for now I added an extra term to count the number of terms in the sequence.
I can check my output against the examples provided on the wikipeadia page.
"""

## num_terms variable to count the number of terms in the sequence. At each step increase its value by 1.
num_terms = 1
## While x is greater than 1, execute the statements in this while loop
while  x > 1:
    # check if current value of x is even and if it is even, divide x by 2 and update x to be this value
    if x % 2 == 0:  
        x = x //2
        ## print the result of this as a term in the sequence 
        print(x) 
        ## increment the term counter variable by 1
        num_terms += 1
        # using a while loop, I no longer need the break clause as the while loop will evaluate to false once x becomes 1
        #if x ==1:
         #   break
        
## however if the current value of x is odd, multiply x by 3 and then add 1 to this product. Update x to be this 
    # here I initially used an elif statement to check if X is odd but an else statement will do as the number x can only be even or odd!
    else:
    # elif x % 2 != 0:
        x = (x * 3) + 1
        # print the result of this as a term in the sequenc
        print(x)
        # increment the term counter variable by 1
        num_terms +=1
## will take this out again. just testing for now. Looking at Wikipeadia page        
print("The number of terms in the sequence is ",num_terms)
   
    
