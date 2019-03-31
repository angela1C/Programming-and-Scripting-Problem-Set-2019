# solution-3.py
# This is my solution to problem 3 on the Problem Set 2019.
# Angela Carpenter
# 31st March 2019

# This program prints all numbers between 1,000 and 10,000 that are divisible by 6 but are not divisible by 12.

# A for loop is used to iterate through every number in a sequence of numbers in the order they appear in the sequence.
# The `range()` function generates a sequence of numbers that can be iterated over in the for loop.

# Using a `for` statement and `range` function to iterate through every integer `i` from 1000 to 10000.
# For each value of i in the range, execute the statements indented after the :
for i in range(1000,10000):
    # check if the value of `i` at each iteration is divisible by 6 or not using modulus operator %
    if (i % 6 ==0):  
        # if above is true then check if i is not divisible by 12, again using the modulus operator
        if(i % 12 !=0): 
            # if the number is divisible by 6 and is not divisible by 12 then print i
            print(i)  




    