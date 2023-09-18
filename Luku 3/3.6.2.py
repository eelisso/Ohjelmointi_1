"""
Eelis Soikkeli, Exercise 3.6.2
Program that prints out the lyrics to a song called Yogi Bear
"""


def repeat_name(name, repeats):
    """ Function that repeats the name of given bear given amount of times """
    for a in range(repeats):
        print(f"{name}, {name} Bear")


def verse(lyrics, name):
    """ Function that prints out the verse """
    print(f"{lyrics}\n"
          f"{name}, {name}\n"
          f"{lyrics}")
    repeat_name(name, 3)
    print(f"{lyrics}\n"
          f"{name}, {name} Bear")


def main():
    verse("I know someone you don't know", "Yogi")
    print("")
    verse("Yogi has a best friend too", "Boo Boo")
    print("")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
