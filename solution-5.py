"""
## Solution to Problem 5 on the Problem Set 2019
# Angela Carpenter
# 23 March 2019

This program asks the user to input a positive integer and in response will tell the user if that number is prime or not.
A prime number is a whole number greater than 1 that is only divisible by itself and 1, that is it's only factors are 1 and the number itself.

To determine if a number greater than 1 is a prime number check if it can be divided, without a remainder, by any number between 2 
and the number itself. Once you find any number at all, that divides into it without a remainder then it is not prime.

My references for working on this problem are as follows:

Python Tutorial  - Section 8.3 Handling Exceptions of the Python tutorial. I used this for the input part of the program.
Python Tutorial  - Section 4.4 break and continue Statements, and else Clauses on Loops
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
The example in section 4.4 was my starting point.

"""
## This part of the code asks the user to input a valid positive integer. 
# If the input is not a positive integer then the user will be asked again and again until a valid positive integer is entered.
while True:
    # While True, execute the `try` statements.
    # If the input is valid, the `break` statement ends this `while` loop skipping the `except` clause of `try`
    try:
        ## ask the user to enter a positive integer and assign it to the variable x
        x = int(input("Please enter a positive integer: ")) 
        # Check if the input was a negative number and if this is true then a `ValueError` is raised. 
        if x < 0:
           raise ValueError
        break  
    except ValueError:
        # if there is a ValueError (either a non-integer or a negative integer) then print the following message
        print("That was not a valid positive integer. Please try again!")

# if the number is 2 then it is a prime number 
if x == 2:
    print(x, "That is a prime")
 # otherwise if the number is not 2
else:
    # for each number in the range starting from 2 up to, but not including the number itself
    for n in range(2,x): 
        # Using the modulus % operator check if that number is evenly divisible by n, in which case the number has a factor besides itself and 1
        if x % n ==0: 
            print(n, "is a factor of ",x, "so it is not prime")
            # break to end the for loop as there is no need to check for any other factors once the first factor is found 
            break  
    else:  
        # This else clause executes when the for loop has fallen through without finding any factors between 2 and the number 
        print(x, "That is prime")

# To verify this program was working ok I checked against a selection of prime numbers at https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers     

