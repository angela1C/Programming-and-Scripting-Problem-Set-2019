# solution-5.py
# This is my solution to Problem 5 on the Problem Set 2019.
# Angela Carpenter
# 31st March 2019


# The first part of the code asks the user to input a valid positive integer. 
# Using try and exception statements, if the input is not valid, the user will be asked again 
# until a valid positive integer is entered.
# If the input is valid, the break statement terminates this while loop 
while True:
    try:
        x = int(input("Please enter a positive integer: ")) 
        # Check if the input was a negative number and if this is true then a ValueError is raised. 
        if x < 0:
           raise ValueError
        break  
    except ValueError:
        # print message if there is a ValueError (either a non-integer or a negative integer).
        print("That was not a valid positive integer. Please try again!")

# if the number is 2 then it is a prime number 
if x == 2:
    print(x, "That is a prime")
 # otherwise if the number is not 2
else:
    # for each number in the range starting from 2 up to, but not including the number itself
    for n in range(2,x): 
        # Check if that number is evenly divisible by n using modulus operator %
        # in which case the number has a factor besides itself and 1
        if x % n == 0: 
            print("That is not prime")
            # break to end the for loop as there is no need to check for any other factors once the first factor is found 
            break  
    else:  
        # This else clause executes when the for loop has fallen through without finding any factors between 2 and the number 
        print("That is prime")

# To verify this program was working ok I checked against a selection of prime numbers 
# at https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers     

