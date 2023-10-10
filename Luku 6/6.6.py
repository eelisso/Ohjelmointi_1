"""
Eelis Soikkeli, exercise 6.6
"""


def reverse_name(name):
    """ Function for reversing name """

    lst = name.split(",")
    lst.reverse()
    stripped = [s.strip() for s in lst if s.strip()]
    string = " ".join(stripped)
    return string
