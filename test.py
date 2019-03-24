
### I am using this script file when I want to try out a few lines of codes
## instead of commenting out lines as I have been doing as I end up with too many
## lines of commented out code in a file!

## working on solution 9

"""
I have this working but now I am going back into sys.py to try and figure out what to do if the file entered is not found
DONT TOUCH THIS!

"""
## first import the sys module
import sys

# if the user has not supplied a filename to the program on the command line prompt them to enter a file
# check if there is an argument entered at the command line. this will be index 1. The program name is an index 0

if len(sys.argv) < 2:

    print("please enter a valid text file for the program to continue")

    try:
        # using this other file entered after promt as the file to read if none entered on running the program
        fileAlt = input("please enter a .txt file ")

    except:
        print("")
    file_to_read = fileAlt


else:
    print(f"go ahead as there are {len(sys.argv)} arguments")
    file_to_read = sys.argv[1]
# at the moment I am still getting an IndexError for 


## unless the filename is entered at the time the program is run this will cause an error so need
# to capture the error before trying to use the expected filename at sys.argv[1]

## happy now with above

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
