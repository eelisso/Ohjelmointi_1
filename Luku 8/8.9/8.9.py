""" Stupid ass alkukommentti for legal reasons """


def main():
    filename = input("Enter the name of the file: ")
    try:
        with open(filename, mode="w") as save_file:
            print("Enter rows of text. Quit by entering an empty row.")
            for n, line in enumerate(iter(input, ''), start=1):
                print(f"{n} {line}", file=save_file)
        print(f"File {filename} has been written.")
    except OSError:
        print(f"Writing the file {filename} was not successful.")


if __name__ == "__main__":
    main()
