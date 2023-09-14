"""
Eelis Soikkeli, tehtävä 3.3
"""


def get_valid_input(data_type, prompt):
    """ Validate user input, take in datatype and input prompt as parameters """
    loop = True
    while loop:  # Create loop for input validation
        try:
            value = data_type(input(prompt).replace(",", "."))
            if value >= 0:
                return value  # Return input value and break loop if input is correct
            else:
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")  # Print out an error and prompt the user again for correct input


count = 0  # Tracker for amount of consecutive "lazy days"

def tracker():
    """ Get user input on number of tracked days and distance ran each day """
    threshold = 0  # Set threshold for "lazy days"
    count = 0  # Tracker for amount of consecutive "lazy days"
    days = get_valid_input(int, "Enter the number of days: ")
    for day in range(1, days + 1):
        length = get_valid_input(float, f"Enter day {day} running length: ")
        if length <= threshold:
            count += 1
            if count >= 3:
                print("\nYou had too many consecutive lazy days!")
                break  # Exit the program
        else:
            count = 0
        runs.append(length)  # Add each iteration to a list called "runs"


def mean_calc():
    """ Calculate the mean of distance ran """
    if count > 3:
        total = 0
        for a in runs:
            total += a
        mean = total / len(runs)
        if mean < 3:
            print(f"\nYour running mean of {mean:.2f} km was too low!")
        else:
            print(f"\nYou were persistent runner! With a mean of {mean:.2f} km.")


runs = []


def main():
    tracker()
    mean_calc()

main()
