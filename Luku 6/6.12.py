"""
Eelis Soikkeli, Exercise 6.12
"""


def count_abbas(text):
    """Function that counts 'abba' substrings"""
    count = 0
    for i in range(len(text) - 3):
        if text[i:i+4] == "abba":
            count += 1
    return count
