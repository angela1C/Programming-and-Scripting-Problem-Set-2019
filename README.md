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
$ python solution-1.py
The program will ask the user to input a postive integer.
The program will output a positive integer containing the sum of all numbers betweem 1 and the number entered  by the user.

## Solution-2.py

This program contains my code for the second problem on the problem set.
2. "Write a program that outputs whether or not today is a day that begins with the letter T. 

To run this program, enter the following command on the command line:
$ python solution-2.py

The program does not require any input from the user.
The program will output a message saying if today begins with a T or not.
"Yes - Today begins with a T" or "No - today does not begin with a T"

## Solution-3.py

This program contains my code for the third problem on the problem set.
3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

To run this program, enter the following command on the command line:
$ python solution-3.py

The program does not require any input from the user.
The program will print all the numbers betweem 1,000 and 10,000 that are divisible by 6 but are not divisible by 12. Any numbers between 1,000 and 10,000 that are divisible by both 6 and 12 are not printed

## Solution-4.py

This program contains my code for the fourth problem on the problem set.

4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
At each step calculate the next value by taking the current value and,if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
Have the program end if the current value is one.

To run this program, go to the command line and enter the following command:
$ python solution-4.py
The program will ask the user to input a postive integer.
The program outputs a sequence of numbers starting with that number as the first term. The rest of the terms are 
calculated from the previous terms by halving the previous term if it was even, or by multiplying the previous term by 3 and adding 1 to this product.
The last number in the sequence is 1

## Solution-5.py

This program contains my code for the fifth problem on the problem set.

5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

To run this program, go to the command line and enter the following command:
$ python solution-5.py
The program will ask the user to input a postive integer. The program will output a message saying if the number is prime or not.

## Solution-6.py

This program contains my code for the sixth problem on the problem set.

6. Write a program that takes a user input string and outputs every second word.

To run this program, go to the command line and enter the following command:
$ python solution-6.py

The program will ask the user to enter a sentence. 
The program will output every second word

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