def tracker():
    runs = []
    days = int(input("Enter the number of days: "))
    if days > 0:
        for day in range(1, days+1):
            length = int(input(f"Enter day {day} length: "))
            if length > 0:
                runs.append(length)
            else:
                print("Run length can't be less than zero.")
        runs.sort()
        print(runs)
    else:
        print("Days can't be zero or less.")

tracker()