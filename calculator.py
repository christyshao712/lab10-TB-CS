import math

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
>>>>>>> 322ec69bcfd6478625fc5a424b37ec5be0e26801

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
    return a^b

