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
https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals for formatted string literals (f-strings)
Python has a format function to convert a value to a “formatted” representation, as controlled by format_spec.
https://stackoverflow.com/a/1598650 for an example of using the format function with keyword arguments
"""
# If the input is not a positive float then the user will be asked again and again until a valid positive integer is entered.
while True:
    ## while True, execute the `try` statements. 
    try:
        rootof = float(input("Please enter a positive floating point number: ")) 
        if rootof < 0:
            ## raise a ValueError if the input is a negative number. 
           raise ValueError
         # break out of the loop to stop asking user for input.
        break  
    ## if an exception does occur within the try clause, then skip the rest of the try statements print exception statement.
    except ValueError:
        print("That was not a positive floating point number. Please try again")

# Assign an intial estimate for the square root. This can be any number to start the loop going
estimate  = 10

# Using Newtons Method, regardless of the starting estimate, once the square of the estimate gets close enough (0.01 here)
# to the actual number itself, then that is a good approximation for the square root. 
# The while loop below will keep changing the estimate until it is close enough, here within 0.01. Then it stops

# The code here using Newtons Method is adapted from  https://tour.golang.org/flowcomtrol/8

# while the absolute difference between the estimate squared and the number in question is greater than 0.01
while abs((estimate * estimate) - rootof )> 0.01:
        # update the estimate using the formula 
    estimate -=((estimate * estimate)-rootof)/(2 * estimate)    
    # the approximation for the square root will be the final value of estimate from the  while loop
 ## assign the final estimate to sqroot   
sqroot = estimate    
    
# can alternatively import math module and use the sqrt function for getting the square root
import math
#print(f"The square root of {rootof} is approx. {math.sqrt(rootof)}.")

# using f-strings with format specifier for the number to be displayed as a fixed point number. 
# The output should be to 1 decimal place as per the sample output.
print(f"The square root of {rootof} is approx. {sqroot:.1f}")

# can also use with keyword arguments as per the Stack overflow post at https://stackoverflow.com/a/1598650
#print(f"The square root of {rootof} is approx.", '{number:.{digits}f}'.format(number=sqroot, digits=1))

