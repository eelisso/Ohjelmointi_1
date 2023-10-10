"""
Eelis Soikkeli, Exercise 6.13
"""

def longest_substring_in_order(text):
    """Function for finding the longest substring"""
    if not text:
        return ""

    current_substring = text[0]
    longest_substring = text[0]

    for i in range(1, len(text)):
        if text[i] >= text[i - 1]:
            current_substring += text[i]
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = text[i]

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring
