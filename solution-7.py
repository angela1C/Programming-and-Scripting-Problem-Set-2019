"""
# Solution to Problem 7 on the Problem Set 2019
# Angela Carpenter
# 23 March 2019

This program contains my code for the seventh problem on the Problem Set 2019:
This program asks the user to input a positive floating point number. It then outputs an approximation of its square root.

There is a python function for calculating square roots in the maths module which is part of the Python Standard Library.
Newtons Method can also be used to get an estimate of the square root of a number.

My references for this program are:

https://docs.python.org/3/library/math.html?highlight=math#module-math for the  sqrt function in the math module.

https://en.wikipedia.org/wiki/Newton%27s_method
https://math.stackexchange.com/questions/350740/why-does-newtons-method-work
https://mathinsight.org/newtons_method_refresher

https://tour.golang.org/flowcontrol/8  
for an explanation of how to use Newtons Method to get the square root of a number

https://docs.python.org/3/library/functions.html#format  for the format function
Python has a format function to convert a value to a “formatted” representation, as controlled by format_spec.
https://stackoverflow.com/a/1598650 for an example of using the format function with keyword arguments
"""
# If the input is not a positive float then the user will be asked again and again until a valid positive integer is entered.
while True:
    ## while True, execute the `try` statements. 
    try:
        x = float(input("Please enter a positive floating point number: ")) 
        if x < 0:
            ## raise a ValueError if the input is a negative number. 
           raise ValueError
         # break out of the loop to stop asking user for input.
        break  
    ## if an exception does occur within the try clause, then skip the rest of the try statements print exception statement.
    except ValueError:
        print("That was not a positive floating point number. Please try again")

# assign the user's input to rootof
rootof= x
# The intial estimate for the square root. This can be any number to start the loop going
estimate  = 10
# count the number of times the loop has to go through to get the square root
iters = 0
# Keep going until the square of estimate is within 0.01 of rootof

 # Using Newtons Method, whatever the starting estimate, once the square of the estimate gets close enough (0.01 here)
 # to the number itself, that is a good approximation for the square root. 

# while loop to keep changing the estimate until it is close enough. Once it is within 0.01 stops
# inner for loop is just to see how many loops it has to do to find the square root
for i in range(1,estimate):
    # while the absolute difference between the estimate squared and the number in question is greater than 0.01
    # This is using Newtons Method to improve our estimate adapted from  https://tour.golang.org/flowcomtrol/8
    while abs((estimate * estimate) - rootof )> 0.01:
        # updates the estimate to the new estimate 
        estimate -=((estimate * estimate)-rootof)/(2 * estimate)
        # printing just for interest to see how many loops it actually takes to get the square root
        print(f"On iteration {iters} of the loop, the square root estimate of {rootof} is {estimate}.")
        # increase the number of iterations by 1 every time it goes around the while loop
        iters += 1
    # the square root is the final value of estimate from the loop above 
    sqroot = estimate    
    
    print(f"Using Newtons Method, and a starting estimate of {i}, the square root of {rootof} is approx. {estimate}.")
    # break here as no need to continue with the for loop once the while loop has evaluated to false.
    # when the estimate for the square root is within 0.01 above
    break

print(f"Using Newtons Method, a starting guess of {i}, it took {iters} loops to find the square root of {rootof} which is approx. {estimate}.")

import math
print(f"Using math.sqrt function, the square root of {x} is approx. {math.sqrt(x)}.")

print(f"The square root of {x} is approx.", '{number:.{digits}f}'.format(number=sqroot, digits=1))
