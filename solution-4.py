"""Write a program that asks the user to input any positive integer and 
outputs the successive values of the following calculation. 
At each step calculate the next value by taking the current value and,
 if it is even, divide it by two, 
 but if it is odd, multiply it by three and add one. 
 Have the program end if the current value is one.
$ python collatz.py

example given of running the program:
Please enter a positive integer: 10
10 5 16 8 4 2 1
----------
user inputs a positive integer x    
if the value of x is even (if x % 2 is 0), divide x by 2
if the value of x is odd (if x % 2 is 1), multiply x by 3 then add 1
if the current value of x is 1 then end program. 

"""
x = int(input("Please enter a positive integer: "))

if x < 0:
    print("Please enter a positive integer")

print(x)

for n in range(x):
    
    if x % 2 == 0:  # if the value of x is even
        x = x //2  ## then divide x by 2 and update x to this value
        print(x) 
        if x==1:  ## if the value of x is 1 then break
            break
# I am putting the break in here because x will only be 1 after 2 /1
# or if the user inputs 1 as the positive integer
# but the break must be in a for or while loop to work
# i tested it with user inputting 1 and it still works
    elif n % 2 ==1:
        x = (x * 3) + 1
        print(x)
    
    
    





