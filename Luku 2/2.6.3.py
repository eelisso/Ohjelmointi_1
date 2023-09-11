"""
Eelis Soikkeli, tehtävä 2.6.3
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            # Use string formatting to ensure each number has a width of 4
            print(f"{i * j:4}", end="")
        print()

main()
