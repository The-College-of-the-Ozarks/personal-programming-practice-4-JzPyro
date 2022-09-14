# logs.py
#
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

import math

def g(x):
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

x = input("Input the value for x between (-10, 7]: ")
x = float(x)

if -10 < x <=7:
    print("g(" + str(x) + ") = " + str(g(x)))
else:
    print("that is not a input between (-10, 7)")
