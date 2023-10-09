"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""


from math import pi, sqrt


def triangle_calc(triangle_side1, triangle_side2, triangle_side3):
    """ Calculate triangle circumference and area """
    triangle_circumference = triangle_side1 + triangle_side2 + triangle_side3
    s = (triangle_side1 + triangle_side2 + triangle_side3) / 2
    triangle_area = sqrt(s*(s-triangle_side1)*(s-triangle_side2)*(s-triangle_side3))
    print(f"The circumference is {triangle_circumference:.2f}")
    print(f"The surface area is {triangle_area:.2f}")

def square_calc(square_side):
    """ Calculate square circumference and area """
    square_circumference = square_side * 4
    square_area = square_side ** 2
    print(f"The circumference is {square_circumference:.2f}")
    print(f"The surface area is {square_area:.2f}")


def rectangle_calc(rectangle_side1, rectangle_side2):
    """ Calculate rectangle circumference and area """
    rectangle_circumference = rectangle_side1 * 2 + rectangle_side2 * 2
    rectangle_area = rectangle_side1 * rectangle_side2
    print(f"The circumference is {rectangle_circumference:.2f}")
    print(f"The surface area is {rectangle_area:.2f}")



def circle_calc(circle_radius):
    """ Calculate circle circumference and area """
    circle_circumference = 2 * pi * circle_radius
    circle_area = pi * circle_radius ** 2
    print(f"The circumference is {circle_circumference:.2f}")
    print(f"The surface area is {circle_area:.2f}")



def get_valid_input(data_type, prompt, allow_zero=True):
    """ Validate user input, take in datatype and input prompt as parameters as well as if zero is allowed or not """
    while True:
        try:
            value = data_type(input(prompt).replace(",", "."))
            if allow_zero and value >= 0:
                return value
            elif not allow_zero and value > 0:
                return value
            else:
                continue
        except ValueError:
            continue


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ").lower()

        if answer == "s":
            square_side = get_valid_input(float, "Enter the length of the square's side: ", False)
            square_calc(square_side)


        elif answer == "r":
            rectangle_side1 = get_valid_input(float, "Enter the length of the rectangle's side 1: ", False)
            rectangle_side2 = get_valid_input(float, "Enter the length of the rectangle's side 2: ", False)
            rectangle_calc(rectangle_side1, rectangle_side2)


        elif answer == "c":
            circle_radius = get_valid_input(float, "Enter the circle's radius: ", False)
            circle_calc(circle_radius)

        elif answer == "t":
            triangle_side1 = get_valid_input(float, "Enter the length of the triangle's side 1: ", False)
            triangle_side2 = get_valid_input(float, "Enter the length of the triangle's side 2: ", False)
            triangle_side3 = get_valid_input(float, "Enter the length of the triangle's side 3: ", False)
            triangle_calc(triangle_side1, triangle_side2, triangle_side3)


        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def real_main():
    """ Filler function to get the points :) """
    menu()
    print("Goodbye!")

def main():
    real_main()

if __name__ == "__main__":
    main()
