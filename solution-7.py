"""
Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

Example of running this program is:
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

"""
## here I set-up a variable 'my_float' to hold the input from the user
my_float = float(input("Please enter a positive floating point number: "))
my_square_root = 0 # set up a variable to hold result

### promt the user to enter a positive float if a negative one is entered
if my_float < 0:
    print("Please enter a positive floating point number")
elif my_float > 0:
    print("You have entered: ",my_float) 

 ## There is an existing maths function called sqrt in the math module
 #  For now I will use this. I'm not sure if I am meant to work it out myself!

import math  ## import the math module
my_square_root = math.sqrt(my_float)

## the sample output in the problem set suggest that we should only return an approximation of the square root
#Here I will round the result of the math.sqrt function
print("The square root of",my_float, "is ",round(math.sqrt(my_float),1))

## I think there is another way of specifying the number of decimal places by using the format function.

""" from the python docs section on floats at https://docs.python.org/3/library/functions.html#float
format(value[, format_spec])
Convert a value to a “formatted” representation, as controlled by format_spec. 
The interpretation of format_spec will depend on the type of the value argument,
 however there is a standard formatting syntax that is used by most built-in types:
  Format Specification Mini-Language.

I found an example of how this is used for floats on stack.overflow which gives an example of how this works at
https://stackoverflow.com/questions/1598579/rounding-decimals-with-new-python-format-function


# {number:.{digits}f}'.format(number=my_square_root, digits=1))
# the nested {digits}  here takes the value of the second argument which is 1 (digits=1) and applies it to the 
precision part of the format
"""
print('{0:.{1}f}'.format(math.sqrt(my_float),1))  ## here the square root of the number is the first argument and the number (argument 0)
# and the number of digits after the decimal point is 1 corresponding to the second argument (argument 1)

## To make this more readable, the post suggests using argument names and passing the corresponding values as keywords arguments to format
print("The square root of ",my_float," is",'{number:.{digits}f}'.format(number=my_square_root, digits=1))





