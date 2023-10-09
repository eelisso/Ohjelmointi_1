"""
Eelis Soikkeli, Exercise 6.14
"""


def format_text(text, max_line_length):
    """ Function for the text formatting """
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:  # Check if adding the word exceeds the line length
            current_line += word + " "
        else:
            lines.append(current_line.strip())  # Remove trailing space and add to lines
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())  # Add the last line

    return "\n".join(lines)


def main():
    print("Enter text rows. Quit by entering an empty row.")
    input_lines = []
    while True:
        line = input()
        if not line:
            break
        input_lines.append(line)

    print("Enter the number of characters per line:", end=" ")
    max_line_length = int(input())

    input_text = "\n".join(input_lines)
    formatted_text = format_text(input_text, max_line_length)

    print(formatted_text)


if __name__ == "__main__":
    main()
