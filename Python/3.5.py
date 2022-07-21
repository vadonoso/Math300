# -*- coding: utf-8 -*-

import math
import sympy as sp
from sympy import cos
from sympy import pi

x = sp.symbols('x')
def f(x):
    return ((x**3)-(cos(pi*x)**2/(2*x**2)+1)+((11/3)*x**2)-1)

print(sp.diff(f(x)))

    