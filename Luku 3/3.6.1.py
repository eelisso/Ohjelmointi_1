"""
Eelis Soikkeli, Exercise 3.6.1
A program that prints out the song 'Old Macdonald Had a Farm'
"""


def print_verse(animal, sound):
    """ A function that prints out the verses """
    print(f"Old MACDONALD had a farm\n"
          f"E-I-E-I-O\n"
          f"And on his farm he had a {animal}\n"
          f"E-I-E-I-O\n"
          f"With a {sound} {sound} here\n"
          f"And a {sound} {sound} there\n"
          f"Here a {sound}, there a {sound}\n"
          f"Everywhere a {sound} {sound}\n"
          f"Old MacDonald had a farm\n"
          f"E-I-E-I-O")


def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
