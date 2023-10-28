"""
Eelis Soikkeli, Exercise 3.8.2
Program that prints out a box with given width, height and mark
Also validates input
"""


def read_input(prompt):
    """ Validate input - break the loop only if value is int value over 0 """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            continue


def print_box(x, y, mark):
    """ Print out the box with given width, height and mark"""
    print()
    for a in range(y):
        print(x*mark)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print_box(width, height, mark)


if __name__ == "__main__":
    main()