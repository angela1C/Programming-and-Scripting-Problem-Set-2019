# Solution to problem 1
""""
This program asks the user to input any positive integer and 
outputs the sum of all numbers between one and that number

This program contains my code for the Programming and Scripting - Problem Set 2019
Question 1: Write a program that asks the user to input any positive integer and 
outputs the sum of all numbers between one and that number.

The inputs that are required  to run this program is a positive integer that the user inputs after being prompted to do so.
The program should output the sum of all numbers between 1 and that number as a single integer

Input must be type integer. What if user inputs a differnt type?
I have looked into this and section 8.3 https://docs.python.org/3/tutorial/errors.html#handling-exceptions
covers exception handling
Also working from Chapter 17 Exceptions of the PythonBook by Peter Spronk at the http://spronck.net/pythonbook/pythonbook.pdf

"""
## This code asks the user to input until a valid positive integer in entered
while True:
    ## while True, the statements between try and except are executed
    ## if there is no exception,the except clause is skipped and the execution of try statement is finished
    try:
        ## ask the user to enter a positive integer 
        x = int(input("Please enter a positive integer: ")) 
        ### here I am accounting for negative integers being entereed
        if x < 0:
            ## raise a ValueError if the input is a negative number
           raise ValueError
         ## break statement breaks out of the loop
        break  
    ## if an exception does occur within the try clause, then skip the rest of the try statements
    #a ValueError is raised when an operation receives an argument of the  right type but an inappropriate value
    except ValueError:
        ## if there is a ValueError print the following message
        print("That was not a valid positive integer. Please try again")
"""
## set up a variable called x to hold the result of the user inputting an integer
#x = int(input("Please enter a positive integer: "))
 # set up a variable called total to hold the total sum
total = 0 
## using a if-elif statements to check if the input is valid.
## if the user inputs an integer less than  or equal to zero then prompt the user to enter a positive integer
if x <= 0:
    print("Please enter a positive integer")
"""

 # set up a variable called total to hold the total sum
total = 0 
## else if the number entered is valid, that is an integer > 0, then go to the next step
# which is the actual calculation

    #A while loop will keep executing while it evaluates to true which is when x >= 1 
    # this program must calculate the sum of all integers betweem 1 and the number.
    # The while loop will finish once the x gets to 1.
while x >= 1:
        # While x >1 add the value of x to total (which is 0 to start) so the total is increasing each time by the value of x
    total += x  
        # for each iteration of the while loop, decrement (reduce) x by 1.
        # This will eventually cause the while to evaluate to false and then the loop will end. 
    x -= 1  
    # finally, once calculation is complete and the total has been calculated, the code is unindented
    # The following print statement will print the final value of total from the while loop. 
print (total)

"""
I have revisted this solution and changed it quite a bit
It is outputting the same result as in the sample output provided in the problem sheet
I am not sure if I need to have the script saved as a particular name such as sumopto.py in the sample output


Input must be type integer. I have now accounted for the user inputting an invalid type
or a negative integer.
My program will no longer result in an error if the user enters a non integer value.
My source for working this out is the Python Tutorial  - Section 8.3 Handling Exceptions of the Python tutorial.
Also Chapter 17 Exceptions of the PythonBook by Peter Spronk at the http://spronck.net/pythonbook/pythonbook.pdf

"""
        



