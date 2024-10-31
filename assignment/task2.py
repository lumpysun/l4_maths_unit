import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

j = cmath.sqrt(-1)
u = (math.sqrt(2) / 1 + j)

x, y = 0, 0j

z_initial = ((math.sqrt(2) * (1 + j))/ (((1 + j) / (math.sqrt(2)))**1))


i = 0
print(int(z_initial.real), z_initial.imag)
while int(z_initial.real) != x or int(z_initial.imag) != y:
    i += 1
    z_initial = (z_initial) / u
    plt.plot(z_initial.real, z_initial.imag, 'ro')
    print(i, z_initial.real, z_initial.imag)

x_label= 'Real'; y_label='Imaginary'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.xlim(-2, 2)
plt.ylim(2,-2)
plt.grid()
plt.show()