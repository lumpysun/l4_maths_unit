import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

j = cmath.sqrt(-1)
e = np.exp(1)
a = 1

x = np.linspace(0,3,1000)
y = (((x-3)*e**((1)/(x-3))/(x*e**(-a*x))))



plt.plot(x,y,'g:')

x_label= 'x'; y_label='y'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.xlim(0, 3)
plt.ylim(-2, 0.25)
plt.grid()
plt.show()