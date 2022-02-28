"""
Module to implement our own calculations
"""

def addition(a, b):
    """
    Implementation of addition operation
    """
    return a+b

def custom_operation(a,b,c):
    """
    Implementation of a custom operation
    """
    return addition(a, soustraction(b,c))

def soustraction(a,b):
    """
    Implementation of soustraction operation
    """
    return a-b
