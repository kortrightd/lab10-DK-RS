"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/kortrightd/lab10-DK-RS.git
# Partner 1: Daniel Kortright
# Partner 2: Ranjith Saravanan

import math


# First example
# Dummy update
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# def divide(a, b):
    # if a == 0:
        # raise ZeroDivisionError
    # else:
        # return a / b

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return a ** b

#import math

def add(a, b): 
    return a+b

def sub(a, b):
    return a-b
    
def mul(a, b):
    return a*b
    
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 1:
        raise ValueError
    return math.log(b, a)
    
def exp(a, b):
    return a ** b


