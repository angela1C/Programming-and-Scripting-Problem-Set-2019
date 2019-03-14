"""
This program is my solution to question 8 on the Problem Set:
Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

Expected Sample Output is as follows:

 $ python datetime.py
Monday, January 10th 2019 at 1:15pm
*****

For this I am referring to the Python Standard Library 
[python library datetime module](https://docs.python.org/3/library/datetime.html#module-datetime)

The Python Tutorial also gives a brief introduction in section 10.8 to Dates and Times
[Section 10.8 Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)

I am also learning from Chapter 27 of the Pythonbook.pdf

Here I am referring to the section "strftime() and strptime() Behavior" 
at https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
Datetime has a method for formatting date objects.
To get the correct format I need the following:
%A weekday name, followed by a comma "," then %B month name full version 
followed by the day of month %d followed by a suffix like th for 10th 
followed by year %y followed by "at" then time using 12 hour clock %I and %p for the suffix of am or pm


"""
# The `datetime` module has a class called datetime an this class has various class methods. 
# To use the functions or class methods of the datetime module, import the datetime module 

#Import the datetime module, as dt for short
import datetime as dt

# using the datetime class of the datetime module, call the class method `datetime.now()`
# assign the result to variable `now`
now =  dt.datetime.now()


print(now.strftime("%A, %B %d %Y at %I:%M%p"))
"""
This format is almost correct, however I need to add a suffix such as 'th' for 5th, 'st' for 1st, 'nd' for 2nd etc.

Write a small script that will append 'st' for 1st, 21st or 31st;
'nd' for 2nd and 22nd, "rd" for 3rd, 23rd, "th" for 4th to 19th and 24th to 30th.

Also %p is returning AM or PM in uppercase where the example shows lowercase so I will have to convert this from upper to lower case
using string method.

From looking at the docs this format depends on the Locale.

"""
# here I strip the day of month from the date stored in now
day = now.strftime("%d")  
# set up a variable for the suffix. Let the default suffix be "th" as this is correct for most days of the month
suf = "th" 
## First use if statement to check if the day is the 1st, 21st or 31st
if day in (1,21,31):  
    # if it is one of these, assing the value 'st' to the suffix variable which will overwrite the default 'th'
    suf = "st"  
    # use elif statement to check if the day is 2nd or 22nd 
elif day in (2,22): 
    ## if the day is day 2 or day 22 then update suf variable to be "nd"
    suf = "nd"  
# after the if-elif statement print the day followed by the suffix
print(day+suf)  

# check to see if the correct suffix is resulting:
print(now.strftime("%A, %B %d %Y at %I:%M%p"))

#Splitting the date and time into two parts and adding the suf variable in between by concatenating using the + operator

print(now.strftime("%A, %B %d")+suf, now.strftime("%Y at %I:%M%p"))
## yes!

## next I need to make the am  or pm part lower case using the string method `.lower()`
print(now.strftime("%I:%M%p").lower())
print(now.strftime("%A, %B %d")+suf, now.strftime("%Y at %I:%M%p").lower())
## result!! come back tomorrow and tidy it up