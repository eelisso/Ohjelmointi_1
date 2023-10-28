""" Kuka helvetti näitä docstringeja jaksaa ees kirjotella tänne """


def main():
    scoreboard = {}
    filename = input("Enter the name of the score file: ")
    exit_program = False
    try:
        with open(filename, mode="r") as file:
            for line in file:
                original = line
                parts = line.split()
                if len(parts) >= 2:
                    player_name = parts[0]
                    try:
                        player_score = int(parts[1])
                    except ValueError:
                        print(f"There was an erroneous score in the file:\n"
                              f"{parts[1]}")
                        exit_program = True
                    if player_name in scoreboard:
                        scoreboard[player_name] += player_score
                    else:
                        scoreboard[player_name] = player_score
                else:
                    print(f"There was an erroneous line in the file:\n"
                          f"{original.rstrip()}")
                    exit_program = True
    except FileNotFoundError:
        print("There was an error in reading the file.")
        exit_program = True
    except Exception as e:
        print(f"An error occurred: {e}")
        exit_program = True

    if exit_program:
        return

    alphabetized = dict(sorted(scoreboard.items()))
    print("Contestant score:")
    for player, score in alphabetized.items():
        print(f"{player} {score}")


if __name__ == "__main__":
    main()
