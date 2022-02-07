while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    func = input("Function: ")

    if func == "1":
        with open("diary.txt", "a") as file:
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            print("Diary saved\n")
    elif func == "2":
        file = open("diary.txt", "r")
        print("Entries:")
        print(file.read())
    elif func == "0":
        print("Bye now!")
        break
