"""
Write a program that outputs whether or not today is a day that begins with the letter T. 
An example of running this program on a Thursday is as follows.

 $ python begins-with-t.py
Yes - today begins with a T.


What are the inputs required? today's date. 
How does it get the input? There is probably a current date function
What the program should do? Take the first letter of the day return from the date function,
Check if it is equal to the string "T" 
Output: a message  saying 'Yes - today begins with a T.' or 'No - today does not begin with a T'

I'm going to look at the date functions on the python tutorial at 'https://docs.python.org/3/tutorial/stdlib.html#dates-and-times'
Also A Whirlwind tour of python book - chapter on built-in types
"""

from datetime import date
now = date.today()
now
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# the strftime seems to strip out the date and time components.
# can I just strip out the day element? Then I need to extract the first letter of the string
today = now.strftime("%A")# assign the day to today
print(today) # yes I can access the name of the day element
print(today[0]) # to access the first letter of the name of the day
if today[0] == "T":
    print("Yes - today begins with a T")
else:
    print("No - today does not begin with a T")
#if now.strftime("%A[1]" == "T"):
 #   print("Yes - today begins with a T")
 

