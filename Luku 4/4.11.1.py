"""
Eelis Soikkeli, Exercise 4.11.1
Program that prints out *cooler* boxes than the previous program
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """ Function for printing out the boxes in question """
    print(width*border_mark)
    for a in range(height-2):
        print(f"{border_mark}{inner_mark*(width-2)}{border_mark}")
    print(width * border_mark)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()