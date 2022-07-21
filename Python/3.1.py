# -*- coding: utf-8 -*-

import scipy as sp

A = sp.array([[1, 2], [3, 4]])
y = sp.array([[5],[8]])

x = sp.linalg.solve(A, y)
print(x)