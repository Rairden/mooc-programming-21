def add(phoneBook: dict, name, num):
    phoneBook[name] = num


def getInput():
    name = input("name: ")
    num = input("number: ")
    return name, num


phoneBook = {}

while True:
    cmd = int(input("command (1 search, 2 add, 3 quit): "))

    if cmd == 1:
        name = input("name: ")
        if name in phoneBook:
            print(phoneBook[name])
        else:
            print("no number")
    elif cmd == 2:
        name, num = getInput()
        add(phoneBook, name, num)
        print("ok!")
    elif cmd == 3:
        print("quitting...")
        break
