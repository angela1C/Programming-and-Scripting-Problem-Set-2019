"""
for question 9 I must read the file in an argument on the command line.
This has led me to learning about Command Line Arguments on the Python Tutorial at 
https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
Common utility scripts often need to process command line arguments. 
These arguments are stored in the sys module’s argv attribute as a list. 

This further led me to the documentation on the sys module at https://docs.python.org/3/library/sys.html#module-sys
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

"""
## first import the sys module
import sys

### print the sys arguments. As there are none other this will just print the program name in a list
print (sys.argv)
## the program or script name is always the first argument in the list

## as there are none other, this will result in IndexError: list index out of range
#print(sys.argv[1])

## Now I am trying to use sys arguments to get the hang of them
a =  "hello "
b = "there "
c = sys.argv[1]  ## this will take the next argument after `python sys.py` on the command line and use it as the second argument
d = sys.argv[2]  ## this will take the second argument after `python sys.py` on the command line and use it as the third argument
#d = "Tony"
print(a + b + "dear ",c + " and dear ",d)

# if either sys.argv[1] or sys.argv[2] are not provided then this will give a 
# IndexError: list index out of range

#I need to see if there can be a default value for the sys.argv.
