import cmath; import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

j = cmath.sqrt(-1)
e = np.exp(1)
a = 1

x = np.linspace(-3,3,1000)
y = np.sqrt((x*(x-1)**2)/(x-2)**2)

plt.plot(x,y,'g:')

x_label= 'x'; y_label='y'
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.xlim(-3,3 )
plt.ylim(-3, 3)
plt.grid()
plt.show()