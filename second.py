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

second(my_testfile.txt)