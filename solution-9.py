"""
# Solution to Problem 9 on the Problem Set 2019
# Angela Carpenter
# 24th March 2019

This program reads in a text file and outputs every second line. 
The program takes the filename of the text file from an argument on the command line.
If the user has not entered a .txt file on the command prompt then they are asked to enter one
This is then used as the file to process.

My references for working on this program are as follows:
Section 7.2 Reading and Writing Files of the Python Tutorial at https://docs.python.org/3/tutorial/inputoutput.html

Python Tutorial section 10.3 Command Line Arguments https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
Also the documentation on the sys module at https://docs.python.org/3/library/sys.html#module-sys

Chapter 17 Exceptions of the PythonBook by Peter Spronk at the http://spronck.net/pythonbook/pythonbook.pdf

To test this I have downloaded the text file version of Moby Dick from the Gutenberg project at http://www.gutenberg.org/ebooks/2489
(Project Gutenberg  offers thousands of free eBooks in various formats - it was the first provider of ebooks)
This will serve as a test file to see if my script works
Also created a shorter text file here with line numbers so I can actually tell if every second line is printing

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
if len(sys.argv) < 2:

    print("please enter a valid text file for the program to continue")

    try:
        # using this other file entered after prompt as the file to read if none initially entered on running the program
        fileAlt = input("please enter a .txt file ")

    except FileNotFoundError:  
        print("PLEASE ENTER A VALID TXT FILE")
    except IndexError:  
        print("INDEX ERROR!")
    # This 
    file_to_read = fileAlt


else:
    # can go ahead as the user did enter an argument along with the program name
    file_to_read = sys.argv[1]

# unless the filename is entered at the time the program is run this will cause an error so need
# to capture the error before trying to use the expected filename at sys.argv[1]

## using with to open the file, this will automatically close the file afterwards
with open(file_to_read,"r") as f:
        # initialise this to count the line numbers
        line_no = 0
    # for every line l in the file object f
        for l in f:
        # add 1 to the line_no to keep track of the number of lines so far
            line_no += 1
        ##if the line_no is even (using modulus operator)
            if (line_no % 2) ==0:
            #print the even lines
                print(l)
"""
I will leave this for now. It is doing what it is meant to be doing but I want to be able to handle the 
case where the file entered is not a valid .txt file. Maybe this is ok as it is as the error message is valid
'FileNotFoundError: [Errno 2] No such file or directory: '  '

The program is taking a text file if one is entered from the command line at the time of running the program.
If there is no argument provided with the script name on the command line, then the user is prompted to enter a file name
This will then be read and processed.
However I have not yet accounted for a file that is not actually available.
I will look more into this and return|!
There is another packages besides the 'sys' package which might be useful. the 'opts' package


"""