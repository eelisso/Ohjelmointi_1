"""
Eelis Soikkeli, Exercise 3.8.1
"""


from math import sqrt


def area(a, b, c):
    """ Function for calculating the area of a triangle """
    s = (a + b + c) / 2
    a = sqrt(s*(s-a)*(s-b)*(s-c))
    return a


def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    print(f"The triangle's area is {area(a,b,c):.1f}")


if __name__ == "__main__":
    main()
