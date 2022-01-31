def printNumbers():
    num = 2
    while num <= 30:
        print(num)
        num += 2


def countdown():
    print("Are you ready?")
    number = int(input("Please type in a number: "))
    while number > 0:
        print(number)
        number -= 1
    print("Now!")


def numbers():
    limit = int(input("Upper limit: "))
    cnt = 1
    while cnt < limit:
        print(cnt)
        cnt += 1


def powersOfTwo():
    limit = int(input("Upper limit: "))
    exp = 1
    val = 1
    while val <= limit:
        print(val)
        val = 2 ** exp
        exp += 1


def powersOfBaseN():
    limit = int(input("Upper limit: "))
    base = int(input("Base: "))
    val = 1
    while val <= limit:
        print(val)
        val *= base


def sum1():
    limit = int(input("Limit: "))
    sum, inc = 1, 2

    while sum < limit:
        sum += inc
        inc += 1

    print(sum)


def sum2():
    limit = int(input("Limit: "))
    sum, inc = 1, 2
    series = "1"

    while sum < limit:
        sum += inc
        series += f" + {inc}"
        inc += 1

    print(f"The consecutive sum: {series} = {sum}")


def strMultiplied():
    str = input("Please type in a string: ")
    amt = int(input("Please type in an amount: "))

    print(str * amt)


def theLongerStr():
    str1 = input("Please type in string1: ")
    str2 = input("Please type in string2: ")

    if len(str1) == len(str2):
        print("The strings are equally long")
    elif len(str1) > len(str2):
        print(f"{str1} is longer")
    else:
        print(f"{str2} is longer")


def endToBeginning():
    str = input("Please type in a string: ")
    index = len(str) - 1

    while index >= 0:
        print(f"{str[index]}")
        index -= 1


def secondToLast():
    str = input("Please type in a string: ")

    if str[1] == str[-2]:
        print("The second and the second to last characters are", str[1])
    else:
        print("The second and the second to last characters are different")


def lineOfHashes():
    width = int(input("Width: "))
    print("#" * width)


def rectOfHashes():
    width = int(input("Width: "))
    height = int(input("Height: "))

    for i in range(0, height):
        print("#" * width)


def underlining():
    while True:
        str = input("Please type in a string: ")
        length = len(str)

        if len(str) == 0:
            return

        print(str)
        print("-" * length)


def rightAligned():
    str = input("Please type in a string: ")
    length = len(str)

    asterisks = 20 - length
    print("*" * asterisks + str)


def framedWord():
    str = input("Word: ")

    width = int((30 - len(str)) / 2)
    print("*" * 30)

    if len(str) % 2 == 0:
        print("*" + " " * (width - 1) + str + " " * (width - 1) + "*")
    else:
        print("*" + " " * (width - 1) + str + " " * width + "*")

    print("*" * 30)


def substrings1():
    str = input("Please type in a string: ")

    # str2 = ""
    # for i in range(0, len(str)):
    # 	str2 += str[i]
    # 	print(str2)

    for i in range(0, len(str) + 1):
        print(str[0:i])


def substrings2():
    str = input("Please type in a string: ")

    for i in range(len(str) - 1, -1, -1):
        print(str[i:])


def vowels():
    str = input("Please type in a string: ")

    if "a" in str:
        print("a found")
    else:
        print("a not found")

    if "e" in str:
        print("e found")
    else:
        print("e not found")

    if "o" in str:
        print("o found")
    else:
        print("o not found")


def firstSubstring():
    word = input("Please type in a word: ")
    char = input("Please type in a character: ")

    idx = word.find(char)
    substr = word[idx:idx + 3]

    if idx != -1:
        if len(substr) >= 3:
            print(substr)


def findAllSubstrings():
    word = input("Please type in a word: ")
    char = input("Please type in a character: ")
    idx = 0

    while idx != -1:
        idx = word.find(char)
        substr = word[idx:idx + 3]
        if len(substr) >= 3:
            print(substr)
            word = word[idx + 1:]
        else:
            return


def secondOccurrence():
    str = input("Please type in a string: ")
    substr = input("Please type in a substring: ")

    idx = str.find(substr)
    if idx == -1:
        print("The substring does not occur twice in the string.")
        return

    str = str[idx + len(substr):]
    idx2 = str.find(substr)

    if idx2 != -1:
        idx2 += idx + len(substr)
        print(f"The second occurrence of the substring is at index {idx2}.")
    else:
        print("The substring does not occur twice in the string.")


def multiplication():
    num = int(input("Please type in a number: "))
    operand1 = 1

    while operand1 <= num:
        operand2 = 1
        while operand2 <= num:
            print(f"{operand1} x {operand2} =", operand1 * operand2)
            operand2 += 1

        operand1 += 1


def firstLetterOfWords():
    str = input("Please type in a sentence: ")
    i = 0

    while True:
        if i >= len(str):
            return
        print(str[i])
        while i < len(str):
            if str[i] != " ":
                i += 1
                continue
            i += 1
            break


def factorial():
    while True:
        num = int(input("Please type in a number: "))
        if num <= 0:
            print("Thanks and bye!")
            return

        val, sum = num, num
        while val > 1:
            val -= 1
            sum *= val
        print(f"The factorial of the number {num} is {sum}")


def flipThePairs():
    num = int(input("Please type in a number: "))

    val = 1
    while val + 1 <= num:
        print(val + 1)
        print(val)
        val += 2

    if val <= num:
        print(val)


def takingTurns():
    num = int(input("Please type in a number: "))

    low = 1
    hi = num
    iters = int(num / 2)

    for _ in range(0, iters):
        print(low)
        print(hi)
        low += 1
        hi -= 1

    if num % 2 != 0:
        print(int(num / 2) + 1)


def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")


def first_character(text):
    print(text[0])


def mean(a, b, c):
    print((a + b + c) / 3)


def print_many_times(text, times):
    for i in range(0, times):
        print(text)


def hash_square(length):
    for i in range(0, length):
        print("#" * length)


def chessboard(length):
    h = 0

    if length % 2 == 0:
        for i in range(1, length + 1):
            for k in range(0, length):
                h += 1
                print(h & 1, end="")
            print()
            h += 1
    else:
        for i in range(1, length + 1):
            for k in range(0, length):
                h += 1
                print(h & 1, end="")
            print()


def squared(str, num):
    idx = 0
    loops = num

    square = num * num
    repeat = int((square / len(str)) + 1)
    longStr = str * repeat

    while loops > 0:
        print(longStr[idx:idx + num])
        idx += num
        loops -= 1


if __name__ == '__main__':
    squared("aybabtu", 5)
    # chessboard(6)
    # hash_square(5)
    # print_many_times("python", 3)
    # mean(1, 2, 3)
    # first_character("gopher")
    # seven_brothers()
    # takingTurns()
    # flipThePairs()
    # factorial()
    # firstLetterOfWords()
    # multiplication()
    # secondOccurrence()
    # findAllSubstrings()
    # firstSubstring()
    # vowels()
    # substrings2()
    # substrings1()
    # framedWord()
    # rightAligned()
    # underlining()
    # rectOfHashes()
    # lineOfHashes()
    # secondToLast()
    # endToBeginning()
    # theLongerStr()
    # strMultiplied()
    # sum2()
    # sum1()
    # powersOfBaseN()
    # powersOfTwo()
    # numbers()
    # countdown()
    # printNumbers()
