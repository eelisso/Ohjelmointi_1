def main():
    try:
        mood = int(input("How do you feel? (1-10) "))
        if mood == 1:
            print("A suitable smiley would be :'(")
        elif 2 <= mood <= 3:
            print("A suitable smiley would be :-(")
        elif 4 <= mood <= 7:
            print("A suitable smiley would be :-|")
        elif 8 <= mood <= 9:
            print("A suitable smiley would be :-)")
        elif mood == 10:
            print("A suitable smiley would be :-D")
        else:
            print("Bad input!")
    except ValueError:
        print("Bad input!")

main()

