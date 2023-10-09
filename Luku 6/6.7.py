"""
Eelis Soikkeli, exercise 6.7
"""


def create_an_acronym(phrase):
    """Function for making the acronyms """
    words = phrase.split()  # Split the phrase into words
    acronym_letters = [word[0].upper() for word in words if word]  # Get the first letter of each non-empty word and convert to uppercase
    return ''.join(acronym_letters)  # Join the letters to form the acronym


