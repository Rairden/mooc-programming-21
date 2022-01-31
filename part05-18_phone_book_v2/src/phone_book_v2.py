def search(phoneBook: dict):
    name = input("name: ")
    if name in phoneBook:
        nums = phoneBook[name]
        for n in nums:
            print(n)
    else:
        print("no number")


def add(phoneBook: dict, name, num):
    if name not in phoneBook:
        phoneBook[name] = []

    phoneBook[name].append(num)


def getInput():
    name = input("name: ")
    num = input("number: ")
    return name, num


def main():
    phoneBook = {}

    while True:
        cmd = int(input("command (1 search, 2 add, 3 quit): "))

        if cmd == 1:
            search(phoneBook)
        elif cmd == 2:
            name, num = getInput()
            add(phoneBook, name, num)
            print("ok!")
        elif cmd == 3:
            print("quitting...")
            break


main()
