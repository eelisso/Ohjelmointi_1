"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").upper()

        if command == "W":

            word = input("Enter the word to be translated: ").lower()
            if word in english_spanish:
                print(f"{word} in Spanish is ")

            print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            add_english = input("Give the word to be added in English: ")
            add_spanish = input("Give the word to be added in Spanish: ")

        elif command == "R":
            remove = input("Give the word to be removed: ")

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
