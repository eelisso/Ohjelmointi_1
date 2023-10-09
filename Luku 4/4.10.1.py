"""
Eelis Soikkeli, Exercise 4.10.1
Program that calculates triangles' angle
"""


def calculate_angle(alpha=None, beta=None):
    """ Function for calculating the angle of a triangle """
    if alpha is None:
        return None
    elif beta is None:
        if alpha < 90:
            return 90 - alpha
    elif alpha + beta < 180:
        return 180 - alpha - beta

