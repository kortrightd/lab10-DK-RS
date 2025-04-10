"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
<<<<<<< HEAD
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return a / b



def logarithm(a, b):
    if a <=:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
=======
import math

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
    if a <= :
        raise ValueError
    return math.log(b, a)
    
def exp(a, b):
>>>>>>> 12f8f37fc97d5593db28b48eb91a96cddbed1ce0
    return a ** b


