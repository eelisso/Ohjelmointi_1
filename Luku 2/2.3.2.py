"""
Eelis Soikkeli, tehtävä 2.3.2
"""
def main():
        number = int(input("Choose a number: "))
        k = 1
        loop = True
        while loop:
            product = number * k
            print(f"{k} * {number} = {number * k}")
            k += 1
            if product >= 100:
                loop = False

main()