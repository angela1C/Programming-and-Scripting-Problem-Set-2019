# Solution-10.py
# This is my solution to Problem 9 on the Problem Set 2019.
# Angela Carpenter 
# 31st March 2019

# This program displays a plot of the functions x, x^2 and 2^x in the range [0, 4].

# Matplotlib is a plotting library for Python. It is not part of the standard library so first needs to be installed.
# see https://matplotlib.org/users/installing.html

# import the matplotlib library and specifically it's pyplot module
import matplotlib.pyplot as pl

# import the numpy library as np for short as the plotting functions from matplotlib expect an np.array
import numpy as np

# create x as a range from 0 to 4. Using numpy array (instead of the list generated from the range function)
# a range from 0 to 4 at steps of 0.1 to make the plots smoother.

x = np.arange(0.,4.,0.1)  

# can plot the functions on the same plot. For every x,y pair of arguments can provide a third optional argument to customise the plot

## first creating an empty figure
fig = pl.figure()

## Add a title to the figure

# writing mathematical equation with math text. 
# use raw strings(precede the quote with an 'r') and surround the math text with dollar signs
pl.suptitle(r'Plotting the functions x, $x^2$ and $2^x$ in the range [0,4]',fontsize = 14)

#pl.plot(x, x,"b",x, x**2,"r", x, 2**x,"g")
pl.plot(x,x, label = r"$f(x)=x$")
pl.plot(x,x**2, label = r"$f(x)=x^2$")
pl.plot(x, 2**x, label = r"$f(x) = 2^x$")
# for each x,y can set an optional third argument for different format styles. The defaults are fine here as it sets a different colour for each line

# Add a label for the X-axis
pl.xlabel('x')
# Add a label for the Y-axis
pl.ylabel("f(x)")

# Also want to add a legend.
pl.legend()

pl.show()


