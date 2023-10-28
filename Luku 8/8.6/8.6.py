""" Stupid ass alkukommentti for legal reasons """


def main():

    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return
    for n, file_line in enumerate(file):
        file_line = file_line.rstrip()
        print(f"{n+1} {file_line}")
    file.close()


if __name__ == "__main__":
    main()
