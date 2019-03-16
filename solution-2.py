"""
This program contains my code for the Programming and Scripting - Problem Set 2019:
"Write a program that outputs whether or not today is a day that begins with the letter T. 
An example of running this program on a Thursday is as follows.

 $ python begins-with-t.py
Yes - today begins with a T.
An example of running it on a Wednesday is as follows.
 $ python begins-with-t.py
No - today does not begin with a T."

I am revisiting my code and tidying it up for the assignment submission.
I have worked on dates and times for problem number 8.

For this problem I am referring to the Python Standard Library 
[python library datetime module](https://docs.python.org/3/library/datetime.html#module-datetime)
https://docs.python.org/3/library/datetime.html#date-objects

The Python Tutorial also gives a brief introduction in section 10.8 to Dates and Times
[Section 10.8 Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)


For this program to run, it needs to take as input the day of the week it is when the program is run. 
For this I can use the datetime module which is part of the Python Standard Library.

The program should take the first letter of the day return from the date function. 
To do this I can extract a substring containing the first element of the day name 
Using an `if` statement and the equality comparison operator `==` to check if the first letter is equal to the string "T" 
If the first letter is a `T` then print one message. 'Yes - today begins with a T.'
If the first letter is not a `T` then print the alternative message 'No - today does not begin with a T'
The program will have a single output which is either a message  saying
 'Yes - today begins with a T.' or 'No - today does not begin with a T'

 There is no need for any exception handling as there is no user input.



"""
## from the datetime module import the date object
from datetime import date
# https://docs.python.org/3/library/datetime.html#date-objects
# the date object has a class method for constructing today's date `date.today()`
# date.today() is a class method for the date object that returns today's date (ie when the program is run)
## using class method `date.today()` to get today's date and assign it to a variable
Today = date.today()

#print(Today)  ## just to test

## date object has a method `strftime` that will return a string representing the date
## according to a format string that is explicitly specified `date.strftime(format)`
# see https://docs.python.org/3/library/datetime.html#datetime.date.strftime

# the strftime returns a formatted string with the the date and time 
# For this program I just need the element for the day of the week.
# (there is a method date.weekday that returns the weekday as an integer
# but I need the actual weekday name.)
# from the object Today, return a string containing the day of the week.
# This is the "%A" part
# Assign this to a variable `Today_day`
Today_day = Today.strftime("%A")

## Use index to access the first element of the name of the day
## extracting the first letter of the day name (at index 0) and using an if statement
## to check if this letter is a "T"
if Today_day[0] == "T":
    ## if the first letter is a T, print this message
    print("Yes - today begins with a T")
    ## if the first letter is not a "T" then print this alternate message
else:
    print("No - today does not begin with a T")

## The program does what it is meant to do - outputs the correct message 
"""
I could do this in less steps and eliminate creating the intermediate variables
I think this might the code more efficient
I will leave both for now and come back later
print(date.today().strftime("%A")[0])
"""

# print(date.today().strftime("%A")[0])
# from the datetime module import the date object
from datetime import date
## using the strftime method to get the format of the string that I need and then using indexing
## to extract the first element which will be the initial of today's day name
## then using an if-else statement to check if this value is equal to "T" or not
# if it is "T" then print one message, if it is not "T" then print the other message
if date.today().strftime("%A")[0] == "T":
    print("Yes - today begins with a T")
else:
    print("No - today does not begin with a T")
