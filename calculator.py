"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
def add(a, b): a + b

def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return None



def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        return None

def exponent(a, b): a ** b



