""" Nice program for nice stuff yes yes very good indeed """


def main():
    word_freq = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    loop = True
    while loop:
        text = input("")
        if text != "":
            words = text.split()
            for word in words:
                word = word.strip('.,!?').lower()
                if word not in word_freq:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
        else:
            loop = False
            sorted_dict = dict(sorted(word_freq.items()))
            for word, count in sorted_dict.items():
                print(f"{word} : {count} times")

if __name__ == "__main__":
    main()