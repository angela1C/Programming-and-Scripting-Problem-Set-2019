"""
Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

 $ python datetime.py
Monday, January 10th 2019 at 1:15pm

Here I am referring to the section "strftime() and strptime() Behavior" 
at https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
Datetime has a method for formatting date objects.
To get the correct format I need the following:
%A weekday name, followed by a comma "," then %B month name full version 
followed by the day of month %d followed by a suffix like th for 10th 
followed by year %y followed by "at" then time using 12 hour clock %I and %p for the suffix of am or pm

"""

## import the datatime module as date
from datetime import date
now = date.today()  ## get todays date and assign it to now
print(now.strftime("%x %X"))

print(now.strftime("%A, %B %d %Y at %I%p"))
"""

I cannot see format in this section of the python docs to append a th or nd or st onto a day of month
as specified in the question I need 10th.
Maybe try write a small script that will append 'st' for 1st, 21st or 31st;
'nd' for 2nd and 22nd, "rd" for 3rd, 23rd, "th" for 4th to 19th and 24th to 30th.
Or check again to see if there is an official way to do this in the documentation
Also %p is returning AM or PM in uppercase where the example shows lowercase.

From looking at the docs this format depends on the Locale.

"""
day = now.strftime("%d")  # strip the day of month from the date
suf = "th"  ## let the default suffix be "th" as this is correct for most dayts of the month
print(day)
if day in (1,21,31):  ## if the day is the 1st, 21st or 31st
    suf = "st"  ## change the suffix to "st"
elif day in (2,22):  ## if the day is 2nd or 22nd
    suf = "nd"  # use the suffux "nd"
print(day,suf)  # print day followed by suffix,

## this is outputting a space between the day and the suffix which i think I need to get rid of
# now i need to figure out how to insert this suffix into the date and time

print(now.strftime("%A, %B %d %Y at %I%p"))

# try splitting the date and time into parts and adding the suf variable.
print(now.strftime("%A, %B %d"),suf, now.strftime("%Y at %I%p"))
# this is working somehwat but I must get rid of the space in between.
daysuf = (now.strftime("%d"),suf)
print(now.strftime("%A, %B %d"),daysuf, now.strftime("%Y at %I%p"))
print(daysuf)
## try str.lstrip([chars]) to Return a copy of the string with leading characters removed. 
#print(daysuf.lstrip())