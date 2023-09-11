"""
Eelis Soikkeli, tehtävä 2.7
"""

def main():

    n = int(input("How many Fibonacci numbers do you want? "))
    n1 = 1
    n2 = 1
    count = 0

    while count < n:
        print(f"{count+1}. {n1}")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

main()
