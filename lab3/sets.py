import math
import numpy

u = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = {1, 2, 3, 4, 5}
b = {1, 3, 5 ,7 ,9}
c = {3, 4, 8, 9}
d = {2, 4, 6 ,8}
e = {3, 5}

from itertools import chain, combinations
def powerset(iterable): 
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(f'AuB = {a.union(b)}')
print(f'AnB = {a.intersection(b)}')
print(f'A\B = {a.difference(b)}')
print(list(powerset(a)))
print(f'AcB = {a.issubset(b)}')
print(f'U ) A = , {u.issuperset(a)}')
