
### I am using this script file when I want to try out a few lines of codes
## instead of commenting out lines as I have been doing as I end up with too many
## lines of commented out code in a file!

## working on solution 9

"""


"""
## first import the sys module
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
## using a try exception here to capture a possible invalid file entered. 
# If a valid text file has been provided then go ahead and process the file
"""
try:
    # using with open so that the file will be closed immediately after the indented block of code has run
    with open(file_to_read,"r") as f:
        # a variable to hold the current line number
        line_no = 0
    ## for every line l in the file object f
        for l in f:
        ## add 1 to the line_no to keep track of the number of lines so far
            line_no += 1
        ## if the line_no is even (using modulus operator)
            if (line_no % 2) ==0:
            ### print the even lines
                print(l)
 # adding an exception error here if the file entered is not valid               
except FileNotFoundError: 
    print("The file entered is not a valid text file")
"""

# now adding a while loop to check that the file read in is a valid file, 
# if it is not then the user is prompted to enter a valid .txt file


while True:
    ## while True, execute the `try` statements. 
    try:
        #file_to_read = input("To continue please enter a single valid .txt file ")
        print(file_to_read)
        with open(file_to_read,"r") as f:
            print(f"file to read is {f}")
        # break out of the loop.     
        continue  
        
    ## if an exception does occur within the try clause, then skip the rest of the try statements and go to the except statements.
    except FileNotFoundError: 
        print("The file entered is not a valid text file")
        file_to_read = input("To continue please enter a single valid .txt file ")
        break

with open(file_to_read,"r") as f:
            print(f"file to read is {f}")
            # a variable to hold the current line number
            line_no = 0
            ## for every line l in the file object f
            for l in f:
        ## add 1 to the line_no to keep track of the number of lines so far
                line_no += 1
        ## if the line_no is even (using modulus operator)
                if (line_no % 2) ==0:
            ### print the even lines
                    print(l)






"""
Here I am taking out the try exception block
# using a try exception block here to capture invalid filename that the user might enter
    try:
        # if no file entered on initially running the program, the text file to read will be this file
        file_to_read = input("please enter a valid .txt file ")
    # exception block for file not found errors if the user enters a file that is not available.
    #except FileNotFoundError:
    except:
        print("PLEASE ENTER A VALID TXT FILE")
        
## if the user inputs more than 1 argument after the program name, alert the user to retry with just a single .txt file
"""
#print(f" the file to be processes is: {file_to_read} arguments")
"""
elif len(sys.argv) > 2:
    print(f" > 2 error: You have entered {len(sys.argv)} arguments. Please try again with a single .txt file")

    try:
        # ask user to enter a single .txt file 
        file_to_read = input("please enter a valid .txt file ")
        ## exception error to handle invalid file name that the user might enter
    except FileNotFoundError:
        print("PLEASE ENTER A VALID TXT FILE")

# if the number of sys arguments is 2, the program name and file name 
else:
    try:
        print(f"=2: go ahead as there are {len(sys.argv)} arguments")
        file_to_read = sys.argv[1]
    except FileNotFoundError:  
        print("PLEASE ENTER A VALID TXT FILE")

## unless the filename is entered at the time the program is run this will cause an error so need
# to capture the error before trying to use the expected filename at sys.argv[1]
#if len(sys.argv) ==2:
 #   try:
 #       print("yeah!")
 #   except FileNotFoundError:  
  #      print("PLEASE ENTER A VALID TXT FILE")

# whichever way we get to here, the file to read is file_to_read
print("yes")
"""
## I am moving the file not found error down here
"""
try:
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
except FileNotFoundError: 
    print("blah the file entered is not a valid text file")
"""