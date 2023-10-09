"""
Eelis Soikkeli, Exercise 4.8.1
Program that compares float numbers
"""


def compare_floats(num1, num2, epsilon):
    """ Function that compares 2 float values against an epsilon """
    return abs(num1 - num2) < epsilon
