"""
Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

$ python divisors.py
1002
1014
1026
etc
9990

Takes all numbers betweem 1000 and 10000
for each number checks if that number is divisible by 6
if yes then check if that number is also divisible by 12
if the number is divisible by 6 but is not divisible by 12 return this number
if the number is divisible by 6 and is also divisible by 12 do not return this


I initially put in extra print statements just to see if my code was working
The program is only to print all the numbers that are divisible by 6  but not 12

"""

for i in range(1000,10000):
    if (i % 6 ==0):  # first checking if i is divisible by 6 using the modulus operator
        if(i % 12 !=0): # if the above is true then check if the number is divisible by 12
            print(i)  ## just for checking now
    



    