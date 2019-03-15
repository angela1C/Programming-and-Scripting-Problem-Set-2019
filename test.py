### I am using this script file when I want to try out a few lines of codes
## instead of commenting out lines as I have been doing as I end up with too many
## lines of commented out code in a file!

## currently working on solution-9.py
# I want to create my own text file with line numbers so that I can test my script
# for solution-9.py and see if it is outputting every second line

##  create a file object for appending to end of file called f
with open("my_testfile.txt","w") as f:
  ## using a for loop to write 100 lines of text with the line number as i
  for i in range(100):
    ## I need to make variable i into a string to avoid TypeError: write() argument must be str, not int
    ## write i as a string so I can get a number on each line
    f.write(str(i))
    ## write a line of text to the file
    f.write(" This is a line in my new file \n")
   
### open the file created above as f
with open("my_testfile.txt") as f:
  ## print the output
  print(f.read())
  


