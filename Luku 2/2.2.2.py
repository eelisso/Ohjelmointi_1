"""
Eelis Soikkeli, tehtävä 2.2.2
"""

def main():
    loop = True
    while loop:
        answer = input("Answer Y or N: ")
        if answer.lower() == "n" or answer.lower() == "y":
            print(f"You answered {answer}")
            loop = False
        else:
            print("Incorrect entry.")
            continue

main()