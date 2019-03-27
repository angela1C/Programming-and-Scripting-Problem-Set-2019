"""
# Solution to Problem 6 on the Problem Set 2019
# Angela Carpenter
# 23 March 2019

This program outputs today's date and time in a the format "Monday, January 10th 2019 at 1:15pm”

My references for working on this problem are the documentation at the Python Standard Library at https://docs.python.org
[python library datetime module](https://docs.python.org/3/library/datetime.html#module-datetime)
Particularly the section "strftime() and strptime() Behavior" https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
The Python Tutorial also gives a brief introduction in section 10.8 to Dates and Times
[Section 10.8 Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)
Also Chapter 27 of the Pythonbook.pdf by Peter Sprock at http://spronck.net/pythonbook/pythonbook.pdf

The program takes the current time and date on your computer at the time the program is run.
It creates a string containing time and date elements in the required format and prints it.
The required format is:
A weekday name, followed by a comma "," then full version of month name followed by the day of month with a suffix for 'th' or 'nd' or 'st'
Then the 4 digit year, followed by the string "at" followed by 24 hour digital clock time with "am" or "pm" at the very end.
followed by year %y followed by "at" then time using 12 hour clock %I and %p for the suffix of am or pm
""" 
# To use the functions or class methods of the datetime module, import the datetime module (as dt for short)
# The `datetime` module has a class called `datetime` and this class has various class methods.
import datetime as dt
# using the datetime class of the datetime module, call the class method `datetime.now()` and assign to `now`
now =  dt.datetime.now()

# use `strftime(format)` to create a string representing the time according to an explicitly specified format string 
#print(now.strftime("%A, %B %d %Y at %I:%M%p"))

# Strip the day of month from the date stored in now
day = now.strftime("%d")  
# Add a suffix such as 'th' for 5th, 'st' for 1st, 'nd' for 2nd etc to get the format shown in the sample
# set up a variable `suf` for this suffix. Let the default suffix be "th" as this is correct for most days of the month
suf = "th" 
## First use if statement to check if the day is the 1st, 21st or 31st of the month, if so replace `th` with `st`
if int(day) in (1,21,31):  
    suf = "st"
    # use elif statement to check if the day is 2nd or 22nd, if so replace `th` with `nd`
elif int(day) in (2,22): 
    suf ="nd"  
elif int(day) == 23:
   suf ="rd" 

# Splitting the date and time into two parts, adding the suf variable in between by concatenating using the + operator, make lowercase
print(now.strftime("%A, %B %d")+suf, now.strftime("%Y at %I:%M%p").lower())


