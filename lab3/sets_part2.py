import cmath 
import math
import numpy as np

j = cmath.sqrt(-1)

b = 0 
c = math.inf
d = 2
e = float('NaN')

set1 = {b, c}
set2 = {d, e}
set3 = {0, +math.inf, math.e**(cmath.log(-j))}

s = set1.union(set2).intersection(set3)

print(s)
