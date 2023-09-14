"""
Eelis Soikkeli, tehtävä 3.3
"""


def get_valid_input(data_type, prompt):  # Validify user input, take in datatype and input prompt as parameters
    loop = True
    while loop:  # Create loop for input validation
        try:
            value = data_type(input(prompt).replace(",", "."))
            if value > 0:
                return value  # Return input value and break loop if input is correct
            else:
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")  # Print out an error and prompt the user again for correct input


def tracker():  # Get user input on number of tracked days and distance ran each day
    threshold = 0  # Set threshold for "lazy days"
    count = 0  # Tracker for amount of consecutive "lazy days"
    days = get_valid_input(int, "Enter the number of days: ")
    for day in range(1, days + 1):
        length = get_valid_input(float, f"Enter day {day} running length: ")
        if length <= threshold:
            count += 1
            if count >= 3:
                print("You had too many consecutive lazy days!")
                exit()  # Exit the program
        else:
            count = 0
        runs.append(length)  # Add each iteration to a list called "runs"


def median_calc():
    runs.sort()  #
    if len(runs) % 2 != 0:  # Odd number of days
        median = runs[len(runs) // 2 + 1]
    else:  # Even number of days
        middle1 = runs[len(runs) // 2 - 1]
        middle2 = runs[len(runs) // 2]
        median = (middle1 + middle2) / 2
    if median < 3:
        print(f"Your running mean of {median:.2f} km was too low!")
    else:
        print(f"You were persistent runner! With a mean of {median} km.")


runs = []
tracker()
median_calc()
