"""
This program asks the user to input any positive integer and 
outputs the sum of all numbers between one and that number

This program contains my code for the Programming and Scripting - Problem Set 2019

The inputs that are required  to run this program is a positive integer that the user inputs after being prompted to do so.
The program should output the sum of all numbers between 1 and that number as a single integer

nput must be type integer. What if user inputs a differnt type?


"""
## set up a variable called x to hold the result of the user inputting an integer
x = int(input("Please enter a positive integer: "))
 # set up a variable called total to hold the total sum
total = 0 
## using a if-elif statements to check if the input is valid.
## if the user inputs an integer less than  or equal to zero then prompt the user to enter a positive integer
if x <= 0:
    print("Please enter a positive integer")
## else if the number entered is valid, that is an integer > 0, then go to the next step
# which is the actual calculation
elif x > 0:
    #A while loop will keep executing while it evaluates to true which is when x >= 1 
    # this program must calculate the sum of all integers betweem 1 and the number.
    # The while loop will finish once the x gets to 1.
    while x >= 1:
        # While x >1 add the value of x to total (which is 0 to start) so the total is increasing each time by the value of x
        total += x  
        # for each iteration of the while loop, decrement (reduce) x by 1.
        # This will eventually cause the while to evaluate to false and then the loop will end. 
        x -= 1  
    #finally, once calculation is complete and the total has been calculated, the code is unindented
    # The following print statement will print the final value of total from the while loop.   
    print(total) 



"""
This is the same code as in my script solution-1.py
"""

        
        




#