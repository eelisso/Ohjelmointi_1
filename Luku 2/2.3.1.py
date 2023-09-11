"""
Eelis Soikkeli, tehtävä 2.3.1
"""
def main():
    number = int(input("Choose a number: "))
    multiplier = 10+1
    for i in range (1,multiplier):
        print(f"{i} * {number} = {i*number}")

main()