"""
Eelis Soikkeli, tehtävä 1.6.9
"""

def main():

    p1 = input("Player 1, enter your choice (R/P/S): ").upper()
    p2 = input("Player 2, enter your choice (R/P/S): ").upper()

    if p1 == p2:
        print("It's a tie!")
    elif p1 == "R":
        if p2 == "S":
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif p1 == "P":
        if p2 == "R":
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif p1 == "S":
        if p2 == "P":
            print("Player 1 won!")
        else:
            print("Player 2 won!")

main()