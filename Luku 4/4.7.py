"""
Eelis Soikkeli, Exercise 4.7
Program for calculating lottery probabilities
"""


def factorial(n):
    """ Function for calculating factorials """
    if n < 2:
        return 1
    else:
        return int(n * factorial(n - 1))


def combinations(n, p):
    """ Calculate the combinations available """
    return int((factorial(n) / (factorial(n-p) * factorial(p))))

def probability():
    """ Print the calculated probability as a fraction """
    while True:
        try:
            n = int(input("Enter the total number of lottery balls: "))
            p = int(input("Enter the number of the drawn balls: "))
            if p < 0 or n < 0:
                print("The number of balls must be a positive number.")
                break
            elif p > n:
                print("At most the total number of balls can be drawn.")
                break
            else:
                print(f"The probability of guessing all {p} balls correctly is 1/{combinations(n,p)}")
                break
        except ValueError:
            continue

def main():
    probability()


if __name__ == "__main__":
    main()

