# https://github.com/christyshao712/lab10-TB-CS.git
# Partner 1: Tanmay Bansal
# Partner 2: Christy Shao

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take the square root of a negative number")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Both sides of the triangle must be numbers.")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b <= 0:
        raise ValueError
    if a <= 0 :
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b


import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a<=1 or b<=0:
        raise ValueError
    return math.log(a,b)

def exp(a, b):
    return a**b