"""
Eelis Soikkeli, tehtävä 2.2.1
"""

def main():
    loop = True
    while loop:
        bored = input("Bored? (y/n) ")
        if bored == "n":
            continue
        elif bored == "y":
            print("Well, let's stop this, then.")
            loop = False
        else:
            print("Incorrect entry")
            continue

main()