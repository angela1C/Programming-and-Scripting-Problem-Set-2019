"""
This program prints all numbers between 1,000 and 10,000 that are divisible by 6 but are not divisible by 12.

This program contains my code for the third problem on the Problem Set 2019:
3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

An example of running this program is as follows:

$ python divisors.py
1002
1014
1026
etc
9990

This program does not need any input from the user.
It should take all of the numbers betweem 1000 and 10000 and for each number 
check if that number is divisible by 6 and if that number is divisible by 6, then check if the number is also divisible by 12.
If the number is divisible by 6 and is also divisible by 12 then return this number
However if the number is divisible by 6 and is also divisible by 12 then do not return this number.

Referring to [Section 4.2 for Statement](https://docs.python.org/3/tutorial/controlflow.html?highlight=range#for-statements) and [section 4.3. The Range() Function](https://docs.python.org/3/tutorial/controlflow.html?highlight=range#for-statements)
of the Python Tutorial.

A For statement is used to iterate through every number in a sequence of numbers in the order they appear in the sequence.
The `range()` function generates a sequence of numbers that can be iterated over in the for loop.

I am assuming from the sample output provided that between 1,000 and 10,000 means starting at 1,000 and up to but not including 10,000
"""

# I am using a `for` statement to iterate through every number from 0 to 1000 in order.
# Using range() to generate a sequence of all integer numbers beginning at 1000, up to but not including 10,000
# `i` is the name of a variable set up to hold each value of the numbers generated from range()
# and for each value of i in the range, execute the statements indented after the :
# https://docs.python.org/3/tutorial/controlflow.html?highlight=range#the-range-function

for i in range(1000,10000):
    # using an if statement to check if the value of `i` at each interation is divisible by 6 or not
    # Using the modulus operator `%` to check if the number is divisible by 6. `==` is the equality operator
    if (i % 6 ==0):  
        ## then check if i is not divisible by 12, again using the modulus operator. `!=` means not equal to
        ## This if clause below is only executed if the if statement above it evaluates to true
        if(i % 12 !=0): 
            # if the number is divisible by 6 and is not divisible by 12 then print i
            print(i)  

"""
This code is producing the same output as in the sample output expected.
    



    