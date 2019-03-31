# solution-4.py
# This is my solution to Problem 4 on the Problem Set 2019
# Angela Carpenter
# 31st March 2019


# This first part of the code asks the user to input a valid positive integer. 
# Using try and exception statements, if the input is not valid, the user will be asked again 
# until a valid positive integer is entered.
# If the input is valid, the break statement terminates this while loop 
while True:
    try:
        x = int(input("Please enter a positive integer: ")) 
        # Check if the input is a negative number and if so then a ValueError is raised. 
        if x < 0:
           raise ValueError   
        break  
    except ValueError:
        # if there is a ValueError (either a non-integer or a negative integer) then print the following message
        print("That was not a positive integer. Please try again!")

# create a list to hold the sequence. x will be the only element at the start
my_seq =[x]
while  x > 1:
    # check if current value of x is even and if it is even, divide x by 2 and update x to be this value
    if x % 2 == 0:  
        x = x //2
        # append x to the my_seq list as the next term in the sequence (instead of printing the term)
        my_seq.append(x)
        
# however if the current value of x is odd, multiply x by 3 and then add 1 to this product. Update x to be this 
    else:
        x = (x * 3) + 1
        # append x to the my_seq list as the next term in the sequence 
        my_seq.append(x)

# unpack the list and print the sequence without brackets. (https://stackoverflow.com/a/35119046)
print(*my_seq, sep = ", ")

 
