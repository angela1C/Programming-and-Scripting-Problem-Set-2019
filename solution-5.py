"""
Write a program that asks the user to input a positive integer and 
tells the user whether or not the number is a prime.

$ python primes.py
Please enter a positive integer: 19
That is a prime.

A prime number is a number that is only divisible by itself and 1.
2 is considered the first prime number.
How to check if a number is prime.
if it is an even number greater than 2 then it is defitely not prime.
if the number can be divided without a remainder by any number between 2
and the number then the number is not prime.

I will remove the additional print statements afterwards. Just to see the output for now
"""
x = int(input("Please enter a positive integer: "))

#if x < 0:
 #   print("Please enter a positive integer")

print("the number you have entered is",x)

if x % 2 == 0:
    print(x, "is divisible by 2 so is not prime") 
else:
    #print(x, "is odd so check if it prime" )
    for n in range(2,x): # start with the number 2
        # and try x modulus n for each number in the range
        if x % n ==0: 
            print( x, "%", n, "is zero so",x," is not prime")
            ## if the remainder is zero then no need to go any further
            break  ## break after the first n that divides without remainder
    else:
        print(x,"is prime")
        ## the result is correct

