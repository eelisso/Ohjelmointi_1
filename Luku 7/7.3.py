"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name: Eelis Soikkeli
Email: eelis.soikkeli@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def price_lookup():
    """ Function for looking up the price """
    loop = True
    while loop:
        price = input("Enter product name: ").strip()
        if price == "":
            print("Bye!")
            loop = False
        elif price in PRICES:
            print(f"The price of {price} is {PRICES[price]:.2f} e")
        else:
            print(f"Error: {price} is unknown.")


def main():
    price_lookup()


if __name__ == "__main__":
    main()
