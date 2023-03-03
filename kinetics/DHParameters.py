import sympy as sym
import numpy

c1, s1, d1 = sym.symbols('c1, s1, d1')
d2 = sym.symbols('d2')
d3 = sym.symbols('d3')


TO = sym.Matrix([[]])
T1 = sym.Matrix([[c1, -s1, 0, 0],
                 [s1,  c1, 0, 0],
                 [0, 0, 1, d1],
                 [0, 0, 0, 1]])

T2 = sym.Matrix([[1, 0, 0, 0],
                 [0, 0, 1, 0],
                 [0, -1, 0, d2],
                 [0, 0, 0, 1]])

T3 = sym.Matrix([[1, 0, 0, 0],
                 [0 ,1 , 0, 0],
                 [0, 0, 1, d3],
                 [0, 0, 0, 1 ]])

Tn = T1*T2*T3



