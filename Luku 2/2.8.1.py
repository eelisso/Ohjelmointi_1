"""
Eelis Soikkeli, tehtävä 2.8.1
"""

def main():
    loop = True
    while loop:
        answer = input("Bored? (y/n) ")
        if answer.lower() == "n":
            continue
        elif answer.lower() == "y":
            print(f"Well, let's stop this, then.")
            loop = False
        else:
            print("Incorrect entry.")
            continue

main()