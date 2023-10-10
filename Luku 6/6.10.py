"""
COMP.CS.100 Programming 1
Code Template
"""

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
    print("The same, shouting:")
    print(upper.upper())



if __name__ == "__main__":
    main()
