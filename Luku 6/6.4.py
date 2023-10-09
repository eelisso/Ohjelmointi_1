"""
Eelis Soikkeli, exercise 6.4
"""


def word_structure():
    """ Function for doing the exercise"""
    word = (input("Enter a word: "))
    vowels = []
    consonants = []
    for character in word:
        if character in "aeiouyAEIOUY":
            vowels.append(character)
        else:
            consonants.append(character)
    print(f'The word "{word}" contains {len(vowels)} vowels and {len(consonants)} consonants.')


def main():
    word_structure()


if __name__ == "__main__":
    main()
