def dict_of_numbers():
    spelledOutNumber = {}

    for i in range(100):
        spelledOutNumber[i] = integerToString(i)

    return spelledOutNumber


def integerToString(num):
    # Returns a spelled out string from a number (41 returns "forty-one")
    words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if num < 20:
        return words[num]

    number = str(num)
    tens = int(number[0]) * 10
    ones = int(number[1])

    if ones == 0:
        return words[tens]

    numToString = f"{words[tens]}-{words[ones]}"
    return numToString


if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
