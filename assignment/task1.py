import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

j = cmath.sqrt(-1)

z_initial = (1+j) / ((math.sqrt(2) * j**4)) * (((1+j) / np.absolute(1+j))**1)

u = (math.sqrt(2) / 1 + j)

def move(z_initial):
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





