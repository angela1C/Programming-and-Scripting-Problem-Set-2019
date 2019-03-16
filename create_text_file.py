## 
# I want to create my own text file with line numbers so that I can test my script
# for solution-9.py and see if it is outputting every second line

## import datetime module and 
import datetime 
# using the datetime module strftime method to create a string called filename from the current date and time
# This creates a filename with the exact date and time wiht .txt at the end
filename = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d-%H-%M-%S.txt")
day = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d-%H-%M-%S")
##  create a file object for appending to end of file called f
with open(filename,"w") as f:
  ## using a for loop to write 100 lines of text with the line number as i
  for i in range(50):
    ## I need to make variable i into a string to avoid TypeError: write() argument must be str, not int
    ## write i as a string so I can get a number on each line
    f.write(str(i))
    ## write a line of text to the file.
    # write can only take exactly one argument
    f.write(" Hello there line number ")  
    f.write(str(i))
    f.write(" in my text file created ")
    f.write(day)
    f.write("\n")