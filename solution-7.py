# solution-7.py
# This is my solution to Problem 7 on the Problem Set 2019.
# Angela Carpenter
# 31st March 2019

# The first part of the code asks the user to input a valid positive floating point number. 
# Using try and exception statements, if the input is not valid, the user will be asked again 
# until a valid positive float is entered.
# If the input is valid, the break statement terminates this while loop 
while True:
    try:
        rootof = float(input("Please enter a positive floating point number: ")) 
        if rootof < 0:
            ## raise a ValueError if the input is a negative number. 
           raise ValueError
         # break out of the loop to stop asking user for input.
        break  
    # if an exception does occur, then skip the rest of the try statements and execute exception statement.
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
 # assign the final estimate to sqroot   
sqroot = estimate    
    
# can alternatively import math module and use the sqrt function for getting the square root
import math
#print(f"The square root of {rootof} is approx. {math.sqrt(rootof)}.")

# using f-strings with format specifier for the number to be displayed as a fixed point number. 
# The output should be to 1 decimal place as per the sample output.
print(f"The square root of {rootof} is approx. {sqroot:.1f}")

