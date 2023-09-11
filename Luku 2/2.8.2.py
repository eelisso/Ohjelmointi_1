"""
Eelis Soikkeli, tehtävä 2.8.2
"""

def main():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for months in range (1,13):
        for days in range (1, days_in_month[months - 1] + 1):
            print(f"{days}.{months}.")

main()