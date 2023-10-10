"""
Eelis Soikkeli, Exercise 6.9
"""


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            encrypted_char = chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_char = chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


def row_encryption(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            encrypted_char = chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_char = chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def read_message():
    """ Function for reading the message """
    text = []
    while True:
        line = input("")
        if line == "":
            return text
        else:
            text.append(line)


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    upper = "\n".join(read_message())
    print("ROT13:")
    text = encrypt(upper)
    print(text)

main()