import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

a = 1

x = np.linspace(0,15,1000)
y = -(math.factorial(a)/x)

plt.plot(x,y,'g:')

x_label= 'x'; y_label='y'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.xlim(0, 15)
plt.ylim(-2, 2)
plt.grid()
plt.show()
