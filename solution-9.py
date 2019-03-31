"""
# Solution to Problem 9 on the Problem Set 2019
# Angela Carpenter
# 31st March 2019

This program reads in a text file and outputs every second line. 
The program takes the filename of the text file from an argument on the command line.
If the user has not entered a .txt file on the command prompt then they are asked to enter one.
This is then used as the file to process.

My references for working on this program are as follows:
Section 7.2 Reading and Writing Files of the Python Tutorial at https://docs.python.org/3/tutorial/inputoutput.html

Python Tutorial section 10.3 Command Line Arguments https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
Also the documentation on the sys module at https://docs.python.org/3/library/sys.html#module-sys

Chapter 17 Exceptions of the PythonBook by Peter Spronk at the http://spronck.net/pythonbook/pythonbook.pdf

To test this I have downloaded the text file version of Moby Dick from the Gutenberg project at http://www.gutenberg.org/ebooks/2489
(Project Gutenberg  offers thousands of free eBooks in various formats - it was the first provider of ebooks)
This will serve as a test file to see if my script works
I also created a shorter text file here with line numbers so I can actually tell if every second line is printing.

"""
# Create a text file with line numbers so that I can test my script

#  create a file object to write to called f
with open("my_testfile.txt","w") as f:
  # using a for loop to write 200 lines of text with the line number as i
  for i in range(200):
    # add a line number starting at 0 to 200
    # convert i to a string to avoid 'TypeError: write() argument must be str, not int'
    f.write(str(i))
    ## write a line of text to the file
    f.write(" This is line number ")
    f.write(str(i))
    f.write(" in my new text file \n")

# Now that I have created a test file with line numbers I can test my script to see if it is outputting every second line
# open the file creating file object f
## first import the sys module
import sys

# if the user has not supplied a filename to the program on the command line prompt them to enter a file
# check if there is an argument entered at the command line. this will be index 1. The program name is an index 0
# if there is only 1 sys argument, then the user has not entered a file name.
# The program needs exactly one .txt file so the length of sys.argvs should be  exactly 2

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