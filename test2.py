import sys

# if the user has not supplied a filename to the program on the command line prompt them to enter a file
# check if there is an argument entered at the command line. this will be index 1. The program name is an index 0

if len(sys.argv) < 2:

    #print("Please enter a valid text file for the program to continue ")
    # ask the user to input a valid text file to continue
    file_to_read = input("please enter a valid .txt file to continue ")

# if the user has entered more than 2 arguments along with the program name:
elif len(sys.argv) > 2:
    # print this message
    print(f"You have entered {len(sys.argv)} arguments. Please try again with a single .txt file")
#   Then ask the user to input a valid text file to continue
    file_to_read = input("To continue please enter a single valid .txt file ")
# if the user has input a single argument along with the program name then can proceed with the program    
else:
    # the file to be processed will be the filename entered on running the program
    file_to_read = sys.argv[1]
print(f"the file to read is {file_to_read}")

# after the above block of code, there should be a file_to_read ready for processing.

# using try except statements to print a proper message if the file inout is not a valid file.
try:

    # open the file to read and execute the indented statements. 
    with open(file_to_read,"r") as f:

            line_no = 0
    ## for every line l in the file object f
            for l in f:
        ## add 1 to the line_no to keep track of the number of lines so far
                line_no += 1
        ## if the line_no is evem (using modulus operator)
                if (line_no % 2) ==0:
            ### print the even lines
                    print(l)
                    
 # print exception error if the file is not valid                   
except FileNotFoundError:
    print("That is not a valid file. The program cannot continue")