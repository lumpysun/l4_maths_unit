import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

j = cmath.sqrt(-1)

z = 1

mpl.rcParams['font.size']=16
plt.plot(z.real, z.imag, 'ro')

print(z)

x_label= 'Real'; y_label='Imaginary'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid()
plt.show()

