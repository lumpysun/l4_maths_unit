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
    Funtion used to move the inspector by iterating through positions
    Arguments:
    z_initial - float
    '''
    z_total = z_initial
    for move in range(1, 64):
        #print(z_initial)
        z_initial = (z_initial) / u
        z_total += z_initial
        #print(z_total)
        plt.plot(z_initial.real, z_initial.imag, 'ro')
    return z_total/64
# Need to calculate the average of positions to find key

# Runs the move function and prints the mean of all positions
print(move(z_initial))

# Grid formating
x_label= 'Real'; y_label='Imaginary'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid()
plt.show()





