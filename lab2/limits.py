# Importing needed libraries
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.size']=14

# Defining array of x values to use
x = np.linspace(0, 125, 1000)
# Defining the Function that is needed
e = np.exp(x)
y_num = (10*e**(5*x)) - (2*e**(-2*x)) + (e**(-x))
y_den = (5*e**(5*x)) + (e**(-2*x))
y = y_num/y_den

# ploting the numerator, denominator and the function
plt.plot(x,y_num,'b-')
plt.plot(x,y_den,'r--')
plt.plot(x,y,'g--')

# Formating and displaying the graph
plt.xlabel('x')
plt.ylabel('y')
plt.yscale('log')
plt.show()
