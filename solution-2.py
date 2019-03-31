# solution-2.py
# This is my solution to problem 2 on the Problem Set 2019.
# Angela Carpenter
# 31st March 2019

# This program outputs whether or not today is a day that begins with the letter T. 

# The datetime module is part of the Python standard library. 
# From the datetime module import the date object.

from datetime import date

# Then using the class method `date.today()` of the date object to get today's date.
# and `strftime` method to get the format of the string for the day of the week.
# From the day of week, get the first letter of the day by extracting the first element at index 0.
# Then use if-else statement to check if this value is equal to "T" or not.
# print appropriate message.

if date.today().strftime("%A")[0] == "T":
    print("Yes - today begins with a T")
else:
    print("No - today does not begin with a T")
