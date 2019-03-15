"""
This script is my solution to Problem 9 of the Problem Set 2019
Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

sample program output:
$ python second.py moby-dick.txt
Title:  Moby Dick; or The Whale
CHAPTER 1
Call me Ishmael.  Some years ago--never mind how long
particular to interest me on shore, I thought I would sail about a
...

For this I will refer to Section 7.2 Reading and Writing Files of the Python Tutorial at https://docs.python.org/3/tutorial/inputoutput.html
The program needs to read in a text file.
Output every second line. I presume starting from the very first line and then skipping every second line.
The program should not cause any changes to the text file it is reading from
It is to take the filename from an argument on the command line.

the python function for opening a file is `open` and it takes the filename as an argument.
The second argument describes the way or mode in which the file will be opened.

To test this I have downloaded the text file version of Moby Dick from the Gutenberg project at http://www.gutenberg.org/ebooks/2489
(Project Gutenberg  offers thousands of free eBooks in various formats - it was the first provider of ebooks)

This will serve as a test file to see if my script works

"""
### the suggested way of opening files is using the `with` keyword.
## The `open()` function is used for opening files. 
# It takes two parameters, a string containing the filename and a string for the mode
# here I am opening the file using read-only mode "r", opening the file as moby as I do not want to make any changes to the file
"""
with open("moby-dick.txt", "r") as moby
    # while the block is indented after the `:` read moby and save into m1
    m1= moby.readline()
 # the file will close automatically. Next print to screen   
print(m1)

## using the `with` keyword to open the text file as file object `f`
with open("moby-dick.txt","r") as f:
    # print the first line
    print(f.readline())
    
## using the `with` keyword to open the text file as file object `f`
with open("moby-dick.txt","r") as f:
    ## for every line l in the file object f
    for l in f:
        # print each line
        print(l)

Next the question asks for every second line to be output
I need to find out if there is a skipline function. 
"""
# how to know how big the file is. 
# I could create a variable to count each line as it is read
# I tried indexing but this does not seem the be allowed
# to get every second line, I could try printing every even line number


## open the file creating file object f
with open("moby-dick.txt","r") as f:
    
    # set up a variable to hold the number of lines
    line_no = 0
    print(type(line_no))
    ## for every line l in the file object f
    for l in f:
        ## add 1 to the line_no to keep track of the number of lines so far
        line_no += 1
        ## if the line_no is evem (using modulus operator)
        if (line_no % 2) ==0:
            ### print the even lines
          print(l)

        # print each line
        #print(l)
        # print the line number
       
## 
# I want to create my own text file with line numbers so that I can test my script
# for solution-9.py and see if it is outputting every second line

##  create a file object for appending to end of file called f
with open("my_testfile.txt","w") as f:
  ## using a for loop to write 100 lines of text with the line number as i
  for i in range(200):
    ## I need to make variable i into a string to avoid TypeError: write() argument must be str, not int
    ## write i as a string so I can get a number on each line
    f.write(str(i))
    ## write a line of text to the file
    f.write(" This is line number ")
    f.write(str(i))
    f.write(" in my new text file \n")

## Now that I have created a test file with line numbers I can test my script to see if it is outputting every second line
## open the file creating file object f
with open("my_testfile.txt","r") as f:
    
    # set up a variable to hold the number of lines
    line_no = 0
    print(type(line_no))
    ## for every line l in the file object f
    for l in f:
        ## add 1 to the line_no to keep track of the number of lines so far
        line_no += 1
        ## if the line_no is evem (using modulus operator)
        if (line_no % 2) ==0:
            ### print the even lines
          print(l)
        
## I am sure there is a better way of doing this. I will come back to this and see if I can improve it
# But for now I will save this.

## I think I need to put it into a function in order to answer the question asked. 
# The program should take the filename from an argument on the command line
# come back to write the function 
## Referring to the Python Tutorial section 4.6 Defining Functions
## https://docs.python.org/3/tutorial/controlflow.html#defining-functions

## using keyword `def` to introduce the function definition, followed by the function name `second`  
# and in parantheses the list of formal parameters, textfile
def second(textfile):
# The statements that form the body of the function must be indented
    ## open the file creating file object f
    with open(textfile,"r") as f:
    
        # set up a variable to hold the number of lines
        line_no = 0
        print(type(line_no))
        ## for every line l in the file object f
        for l in f:
            ## add 1 to the line_no to keep track of the number of lines so far
            line_no += 1
            ## if the line_no is evem (using modulus operator)
            if (line_no % 2) ==0:
                ### print the even lines
            print(l)

# I have copied my function into a separate python script second.py
# it is not finised but I will leawe it for tonight.