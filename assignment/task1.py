import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

# Define J (sqrt of -1)
j = cmath.sqrt(-1)

# Define equation for the initial position of the inspector
z_initial = (1+j) / ((math.sqrt(2) * j**4)) * (((1+j) / np.absolute(1+j))**1)

# Define variable u to use in iteration
u = (math.sqrt(2) / 1 + j)

def move(z_initial):
    '''
    funtion used to move the inspector by iterating through positions
    Arguments:
    z_initial - float
    '''
    for move in range(1, 64):
        print(z_initial)
        z_initial = (z_initial) / u
        plt.plot(z_initial.real, z_initial.imag, 'ro')


move(z_initial)
x_label= 'Real'; y_label='Imaginary'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid()
plt.show()





