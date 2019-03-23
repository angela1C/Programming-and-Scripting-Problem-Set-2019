"""
# Solution to problem 3 on the Problem Set 2019
# Angela Carpenter 23 March 2019
# This program prints all numbers between 1,000 and 10,000 that are divisible by 6 but are not divisible by 12.

This program goes through all of the integers between 1000 and 10000.
For each number it one checks if it is divisible by 6 and if it is it then checks if the number is not divisible by 12.
If the number is divisible by 6 and is also not divisible by 12 then this number is returned.
However if the number is divisible by 6 and is also divisible by 12 then do not return this number.

Referring to [Section 4.2 for Statement](https://docs.python.org/3/tutorial/controlflow.html?highlight=range#for-statements) and [section 4.3. The Range() Function](https://docs.python.org/3/tutorial/controlflow.html?highlight=range#for-statements)
of the Python Tutorial.

A For statement is used to iterate through every number in a sequence of numbers in the order they appear in the sequence.
The `range()` function generates a sequence of numbers that can be iterated over in the for loop.
"""

# Using a `for` statement and `range` function to iterate through every integer `i` from 1000 to 10000 in order.
# For each value of i in the range, execute the statements indented after the :
for i in range(1000,10000):
    # using an `if` statement and the modulus operator `%` to check if the value of `i` at each iteration is divisible by 6 or not
    if (i % 6 ==0):  
        # if it is true then then check if i is not divisible by 12, again using the modulus operator
        if(i % 12 !=0): 
            # if the number is divisible by 6 and is not divisible by 12 then print i
            print(i)  




    