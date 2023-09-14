def get_valid_input(prompt):
    loop = True
    while loop:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input.")

def tracker():
    runs = []
    threshold = 0
    count = 0
    days = get_valid_input("Enter the number of days: ")
    for day in range(1, days+1):
        length = get_valid_input(f"Enter day {day} running length: ")
        if length <= threshold:
            count += 1
            if count >= 3:
                print("You had too many consecutive lazy days!")
                exit()
        else:
            count = 0
        runs.append(length)

    runs.sort()
    if days % 2 == 1:
        median = runs[days // 2]
    else:
        middle1 = runs[days // 2 - 1]
        middle2 = runs[days // 2]
        median = (middle1 + middle2) / 2
    if median < 3:
        print(f"Your running mean of {median} km was too low!")
    else:
        print(f"You were persistent runner! With a mean of {median} km.")

tracker()