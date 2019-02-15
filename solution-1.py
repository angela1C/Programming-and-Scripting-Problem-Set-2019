# Solution to problem 1
""""
Write a program that asks the user to input any positive integer and 
outputs the sum of all numbers between one and that number.
break it down into the different parts.

what are the basic ingredients we need?
list them at the top
what are the steps we need to take
python can do a repetitive thing while a condition is true
at the end print out the result
 What are the inputs that are required  for this exercise: a positive integer
What are the expected outputs: the sum of all numbers between 1 and that number
how to get the program to accept the user input
what variables should the program have stored already?
#what is the program to calulate

#input must be type integer. What if user inputs a differnt type?
# 

#looking at the tutorial at https://docs.python.org/3/tutorial/controlflow.html
"""
x = int(input("Please enter a positive integer: "))
total = 0 # set up a variable to hold the total sum

if x < 0:
    print("Please enter a positive integer")
elif x > 0:
    print("You have entered: ",x) # 5

    while x >= 1: # while the number entered is > 1
        total = total + x  # add the number to to total 0 + 5
        x = x - 1  # reduce x by 1 = 4
    print ("The sum of all numbers between your number",x, "and 1 is ",total)



# need to clarify if between 1 and that number includes 1
# 5+4+3+2+1 or 5+4+3+2

        
        



