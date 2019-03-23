"""
# Solution to problem 2 on the Problem Set 2019
# This program outputs whether or not today is a day that begins with the letter T. 

For this I referred to the sections on the `datetime` module in the Python Standard Library and the Python Tutorial, both at https://docs.python.org
[python library datetime module](https://docs.python.org/3/library/datetime.html#module-datetime) and https://docs.python.org/3/library/datetime.html#date-objects
The Python Tutorial also gives a brief introduction in section 10.8 to Dates and Times [Section 10.8 Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)

For this program to run, it takes as input the actual day of the week when the program is run. The datetime module, part of the Python Standard Library, can do this.
The program needs the first letter of the day returned from the date function. It extracts a substring containing the first element of the day name.
Date object has a method `strftime` that will return a string representing the date according to a format string that is explicitly specified `date.strftime(format)`
Then using `if` statement and the equality comparison operator `==` to check if the first letter extracted in the sub-string is equal to the string "T" or not.
If it is then print one message. If not, it prints the alternative message. 
The program will have a single output which is either a message  saying 'Yes - today begins with a T.' or 'No - today does not begin with a T'

"""
# from the datetime module import the date object
from datetime import date
# Using class method `date.today()` of the date object to get today's date, then using `strftime` method to get the format of the string for the day of the week.  
# From the day of week, get the first letter of the day by extracting the first element at index 0.
# Then use if-else statement to check if this value is equal to "T" or not
if date.today().strftime("%A")[0] == "T":
    # if it is "T" then print this message
    print("Yes - today begins with a T")
else:
    #if it is not "T" then print the other message
    print("No - today does not begin with a T")
