""" The stupid ass docstring AGAIN only for legal reasons """


def main():

    scoreboard = {}

    filename = input("Enter the name of the score file: ")
    with open(filename, mode="r") as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2:
                player_name = parts[0]
                player_score = int(parts[1])
                if player_name in scoreboard:
                    scoreboard[player_name] += player_score
                else:
                    scoreboard[player_name] = player_score

    alphabetized = dict(sorted(scoreboard.items()))
    print("Contestant score:")
    for player, score in alphabetized.items():
        print(f"{player} {score}")


if __name__ == "__main__":
    main()
