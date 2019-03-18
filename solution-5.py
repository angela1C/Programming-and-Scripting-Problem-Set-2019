"""
This program asks the user to input a positive integer and in response will tell the user if that number is prime or not.

This program contains my code for the fifth problem on the Problem Set 2019:
5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

An example given of running this program:
$ python primes.py
Please enter a positive integer: 19
That is a prime.

A prime number is a whole number greater than 1 that is only divisible by itself and 1, that is it's only factors are 1 and the number itself.
The number 2 is considered the first prime number.

How to check if a number is a prime number.
First check if the number is a whole number greater than 1
If a number is even and greater than 2 then it is definitely not prime.
If a number can be divided, without a remainder, by any number between 2 and the number then the number is not prime.

I will remove the additional print statements afterwards. Just to see the output for now

My sources for working on this problem are as follows:

Python Tutorial  - Section 8.3 Handling Exceptions of the Python tutorial. I used this for the input part of the program.
Python Tutorial  - Section 4.4 break and continue Statements, and else Clauses on Loops
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
The example in section 4.4 was the starting point

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

# if the number is 2 then it is a prime number 
if x == 2:
    print(x, "That is a prime")
 # otherwise if the number is not 2
else:
    # for each number in the range from 2 up to but not including the number itself
    for n in range(2,x): 
        # Using the modulus operator check if that number is evenly divisible by n, in which case the number has a factor besides itself and 1
        if x % n ==0: 
            ## print statement for now. 
            print(n, "is a factor of ",x, "so it is not prime")
            # break as there is no need to check for any other factors once this is true as the number cannot be prime
            break  
    else:  
        ## This else clause executes when the for loop above has fallen through without finding any factors between 3 and the number 
        print(x, "That is prime")
    ##         

