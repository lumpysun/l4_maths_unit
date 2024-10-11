import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

j = cmath.sqrt(-1)

a = (4-4j)
b = (2j)*(1+2j)**2
z = -j *(a/b)

n = 1001
for i in range(1,n):
    print(i)
    new_val = (j**i) * z
    mpl.rcParams['font.size']=16
    plt.plot(new_val.real, new_val.imag, 'ro')

x_label= 'Real'; y_label='Imaginary'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid()
plt.show()
