"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    alphabetical = sorted(english_spanish)
    dictionary_contents = ", ".join(alphabetical)
    print(f"Dictionary contents:\n"
          f"{dictionary_contents}")

    while True:


        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").upper()

        if command == "W":

            word = input("Enter the word to be translated: ").lower()
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            add_english = input("Give the word to be added in English: ")
            add_spanish = input("Give the word to be added in Spanish: ")
            english_spanish[add_english] = add_spanish
            alphabetical = sorted(english_spanish)
            dictionary_contents = ", ".join(alphabetical)
            print(f"Dictionary contents:\n"
                  f"{dictionary_contents}")

        elif command == "R":
            remove = input("Give the word to be removed: ")
            if remove in english_spanish:
                del english_spanish[remove]
            else:
                print(f"The word {remove} could not be found from the dictionary.")

        elif command == "P":
            sorted_dict = dict(sorted(english_spanish.items()))
            print("\nEnglish-Spanish")
            for i in sorted_dict:
                print(i, sorted_dict[i])
            flipped_dict = {v: k for k, v in sorted_dict.items()}
            sorted_flipped = dict(sorted(flipped_dict.items()))
            print("\nSpanish-English")
            for i in sorted_flipped:
                print(i, sorted_flipped[i])
            print("")

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ").split()
            translated_words = [english_spanish.get(word, word) for word in text]
            spanish_text = ' '.join(translated_words)
            print(f"The text, translated by the dictionary: \n"
                  f"{spanish_text}")

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
