"""
Eelis Soikkeli, Exercise 3.6.3
Program that prints out cool boxes
"""


def print_box(x, y, sign):
    """ Function for printing out the *cool* boxes """
    for a in range(y):
        print(f"{x*sign}")


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
