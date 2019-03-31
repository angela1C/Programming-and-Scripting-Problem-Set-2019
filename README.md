# Problems sets solutions

This repository contains my solutions to the Problem Set 2019 for the module Programming and Scripting at GMIT as part of the Higher Diploma in Computing and Data Analytics.
The pdf file containing the problem set instructions is available at:
[Problem Set 2019](https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf)

## How to download this repository.

1. Go to the URL for the repository on GitHub at https://github.com/angela1C/pands-problem-set
2. Click the green `Clone or download` button.

## How to run the code
Make sure you have `Python 3` installed. 
If not go to https://www.python.org/downloads/ and follow the instructions.

The instructions for running each program are listed below. 
There are ten python programs, one for each of the questions on the problem set. Each program is entitled `solution-x.py` with the number indicating which question the python program pertains to. For example, `solution-1.py` is the program solution for `Question 1` on the problem set.

To run each python program, first navigate to the folder downloaded from this repository. 

At the command line enter `python <program_name>`
for example: $ python solution-1.py
Follow any instructions that are printed to the screen.

## References

The online documentation provided at the Python.org website has been my main reference point for this project.  
In particular, [The Python Tutorial](https://docs.python.org/3/tutorial/) for learning the basics about the Python language and for some code examples of the various concepts but also [The Python Standard Library](https://docs.python.org/3/library/index.html) for more details.

 "The Coder's Apprentice: Learning Programming with Python" by Pieter Spronck at http://spronck.net/pythonbook/pythonbook.pdf. This book has also been very helpful for learning python programming.

[matplotlib documentaion](https://matplotlib.org/tutorials/introductory/pyplot.html)

I did various internet searches for some of the mathematical terms that arose in this assignment such as The Collatz Conjecture, Prime Numbers, Newton's Method etc to ensure I was applying the terms correctly and also for testing the results of running my code.

For this I found Wikipedia's wikis quite useful plus [StackExchange.com](https://stackexchange.com) and [Mathsinsight.org](https://mathinsight.org).


https://en.wikipedia.org/wiki/Collatz_conjecture for solution-4.py
https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers for solution-5.py
https://en.wikipedia.org/wiki/Newton%27s_method for solution-7.py
https://math.stackexchange.com/questions/350740/why-does-newtons-method-work for solution-7.py
https://mathinsight.org/newtons_method_refresher for solution-7.py



## Solution-1.py
This program contains my code for the first problem on the problem set.
1. Write a program that asks the user to input any positive integer and 
outputs the sum of all numbers between one and that number.

To run this program, go to the command line and enter the following command:
`$ python solution-1.py`.  
The program will ask the user to input a positive integer.
The program will output a positive integer containing the sum of all numbers between 1 and the number entered  by the user.

The input can be any positive integer. If the user inputs something other than this an error message is printed until a positive integer is entered.  
For this I referred to the Python Tutorial - [Section 8.3 Handling Exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) 
and [The Python Standard Library Documentation](https://docs.python.org/3/library/exceptions.html#ValueError).  
I also referred to Chapter 17 Exceptions of the PythonBook by Peter Spronk at the http://spronck.net/pythonbook/pythonbook.pdf.   
A `ValueError` is raised to capture a negative integer being input.


## Solution-2.py

This program contains my code for the second problem on the problem set.  
2. Write a program that outputs whether or not today is a day that begins with the letter T. 

To run this program, enter the following command on the command line:  
`$ python solution-2.py`

The program does not require any input from the user.
The program will output a message saying if today begins with a T or not.
"Yes - Today begins with a T" or "No - today does not begin with a T"

For this problem I referred to the sections on the `datetime` module in the Python Standard Library and the Python Tutorial, both at https://docs.python.org.
[python library datetime module](https://docs.python.org/3/library/datetime.html#module-datetime) and https://docs.python.org/3/library/datetime.html#date-objects.  
The Python Tutorial also gives a brief introduction in section 10.8 to Dates and Times [Section 10.8 Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times).

For this program to run, it takes as input the actual day of the week when the program is run. The `datetime` module, part of the Python Standard Library, can do this. The `date` object of `datetime` is used here and it's class method `date.today()` is used to get today's date - the date when the program is actually run.
The program requires only the first letter of the day returned from the `date`. It extracts a substring containing the first element of the day name.
The `date` object has a method `strftime` that will return a string representing the date according to a format string that is explicitly specified `date.strftime(format)`. 
The program then checks if the first letter is equal to "T" or not and prints the appropriate message.


## Solution-3.py

This program contains my code for the third problem on the problem set.  

3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

To run this program, enter the following command on the command line:
`$ python solution-3.py`

The program does not require any input from the user.

For writing this program, I referred to [Section 4.2 for Statement](https://docs.python.org/3/tutorial/controlflow.html?highlight=range#for-statements) and [section 4.3. The Range() Function](https://docs.python.org/3/tutorial/controlflow.html?highlight=range#for-statements)
of the Python Tutorial.

A `for`  loop is used to iterate through every number in a sequence of numbers in the order they appear in the sequence.
The `range()` function generates a sequence of numbers that can be iterated over in the for loop.

The program will print all the numbers between 1,000 and 10,000 that are divisible by 6 but are not divisible by 12. Any numbers between 1,000 and 10,000 that are divisible by both 6 and 12 are not printed.

This program goes through all of the integers between 1000 and 10000. For each number it first checks if it is divisible by 6 and if it is, then it checks if the number is not divisible by 12.
If the number is divisible by 6 and is also not divisible by 12 then this number is printed.
However if the number is divisible by 6 and is also divisible by 12 then this number is not printed.

## Solution-4.py

This program contains my code for the fourth problem on the problem set.

4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.  

To run this program, go to the command line and enter the following command:
`$ python solution-4.py`.     
The program will ask the user to input a postive integer.    

It outputs a sequence of numbers starting with that number as the first term. The rest of the terms in the sequence are calculated from the previous terms by halving the previous term if it was even or by multiplying the previous term by 3 and adding 1 to this product if the previous term was odd. The last number in the sequence is 1.

As this problem relates to the Collatz Conjecture, I referred to wikipedia at https://en.wikipedia.org/wiki/Collatz_conjecture for some information on it.    
The Examples section on the Wikipedia page provided some examples with the exact seqeunces that should be generated for a particular number. I used this to test that my code was generating the correct sequences.  

I also referred to various sections of the Python Tutorial to write this program.  
- [Python Tutorial  - Section 8.3 Handling Exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions).
- [Python Tutorial  - Section  4.4 break and continue statements](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)   
- [Python Tutorial - Section 3.2 First Steps Towards Programming](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)


Similarly to `solution-1.py`, the input must be a positive integer. If the user inputs something other than this an error message is printed until a positive integer is entered using `try` and `except` statements. A `ValueError` is raised to capture a negative integer being input.

This program uses a `while` loop and `if-else` statements to check if the previous number in the sequence is even or odd. 
To produce output in the same format as the sample output provided on the [Problem Set 2019](https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf)  I used a `list` to hold the terms of the sequence. The next term in the sequence is appended to the end of the list. 

To remove the brackets from the list I referred to a [stackoverflow post](https://stackoverflow.com/a/35119046) which suggested using the `*` to unpack the list.




## Solution-5.py

This program contains my code for the fifth problem on the problem set.

5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

To run this program, go to the command line and enter the following command:  
`$ python solution-5.py`  
The program will ask the user to input a postive integer. The program will output a message saying if the number is prime or not.

A prime number is a whole number greater than 1 that is only divisible by itself and 1, that is it's only factors are 1 and the number itself.

To determine if a number greater than 1 is a prime number check if it can be divided, without a remainder, by any number between 2 and the number itself. Once you find any number at all, that divides into it without a remainder then it is not a prime number.

My references for working on this problem are as follows:

[Python Tutorial  - Section 4.4 break and continue Statements, and else Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops). 
The example in section 4.4 was my starting point for writing the code for this program. 

To verify this program was working ok I checked against a selection of prime numbers at https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers. 
   

## Solution-6.py

This program contains my code for the sixth problem on the problem set.

6. Write a program that takes a user input string and outputs every second word.

To run this program, go to the command line and enter the following command:  
`$ python solution-6.py`

This program asks the user input a string and it will output every second word.
It takes a string input by the user, then splits the string into words. A word here it taken as one or more characters separated by a space.  
Go through the list of words but only print every second one.
It does so using indexing to go through each word in the list of words starting from the very first word, ending at the very last word, using a step size of 2 to get every second word. It then concatenate every second word in other_word with whitespace using the `str.join()` method.

My references for working on this problem are as follows:
[Section 3.1.2 of The Python Tutorial](https://docs.python.org/3/tutorial/introduction.html#strings)
[String Methods in the Python Standard Library](https://docs.python.org/3/library/stdtypes.html#string-methods)
In particular:
[str.split()](https://docs.python.org/3/library/stdtypes.html#str.split) and [str.join](https://docs.python.org/3/library/stdtypes.html#str.join)

## Solution-7.py

This program contains my code for the seventh problem on the problem set.

To run this program, go to the command line and enter the following command:
$python solution-7.py

The program will ask the user to enter a positive floating point number.
The program will output the approximate square root of the number.



## Solution-8.py
This program contains my code for the eight problem on the problem set.

This program outputs today's date and time in a the format "Monday, January 10th 2019 at 1:15pm”

To run this program, go to the command line and enter the following command:
$ python solution-8.py

## Solution-9.py
This program contains my code for the ninth problem on the problem set.
This program reads in a text file and outputs every second line. 
The program takes the filename from an argument on the command line

To run this program, go to the command line and enter the following command:
$ python solution-9.py `<file.txt>`

Note if the text file is not in the same directory as `solution-9.py` then you should provide the full path to the file.


## Solution-10.py

This program contains my code for the tenth problem on the problem set.

10. Write a program that displays a plot of the functions x, x^2 and 2^x in the range[0,4]

To run this program, go to the command line and enter the following command:
$ python solution-10.py

The program will generate the plot of the three functions. 

Note to return to the command line you must first close out of the resulting plot. 