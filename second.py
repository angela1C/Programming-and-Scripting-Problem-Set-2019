"""
Here is my working code from solution-9.py
The question asks for the program to take the filename from an argument on the command line
my solution is currently supplying the file to open as an argument within the program

"""
# The program seems to be giving the correct output so the only thing I am looking to change for now is
# to get the program to get the filename to be processed by the script from the command line.

# I am referring to the relevant secion of the Python Tutorial [section 10.3 Command Line Arguments]https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
# "Common utility scripts often need to process command line arguments. These arguments are stored in the sys module’s argv attribute as a list." 
# the first argument in the list, `argv[0]` will be the name of the script

## This leads me to the Python Standard Library documentation for the `sys` module at https://docs.python.org/3/library/sys.html#module-sys
import sys
# The first sys argv, at the start of the list of arguments at argv[0] will be the script name.
# any other other arguments will be next in the argv list.
print(sys.argv)

# initially I added the filename as a string to the open function.
# with open("filename.txt","r") as f:
# instead now I am going to substitute the filename in the script with `argv[1]` 
# Then the program can take the filename from an argument on the command line
with open(sys.argv[1],"r") as f:

 # this part of the code is doing what I want so I will leave for now   
    # set up a variable to hold the number of lines
    line_no = 0
    ## for every line l in the file object f
    for l in f:
        ## add 1 to the line_no to keep track of the number of lines so far
        line_no += 1
        ## if the line_no is evem (using modulus operator)
        if (line_no % 2) ==0:
            ### print the even lines
          print(l)

"""
The question asks for the program to take the filename from an argument on the command line
Above I am giving the file to open to the program within  the program
"""
# referring to [section 10.3 Command Line Arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)

# the sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. 
import sys
# print the list if command line arguments passed to this script.
# The first argv[0] is the script name so in this case second.py
print(sys.argv)



## when I run the above, it prints out the two arguments in this program.
## which are the name of this program `second.py` and `test1.txt` which is the only other argument givem
# argv[0] is the name of the script `second.py`