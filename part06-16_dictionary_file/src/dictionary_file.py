def buildDict():
    finnToEng = {}
    with open("dictionary.txt", "r") as f:
        for line in f:
            ln = line.replace("\n", "").split(";")
            finnToEng[ln[0]] = ln[1]

    return finnToEng


def main():
    finnToEng = buildDict()

    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        cmd = input("Function: ")

        if cmd == "1":
            finWord = input("The word in Finnish: ")
            engWord = input("The word in English: ")
            finnToEng[finWord] = engWord
            open("dictionary.txt", "a").write(f"{finWord};{engWord}\n")
            print("Dictionary entry added")
        elif cmd == "2":
            search = input("Search term: ")
            for i, k in finnToEng.items():
                if search in i or search in k:
                    print(f"{i} - {k}")
        elif cmd == "3":
            print("Bye!")
            break


main()
