def most_common_character(string):
    mostCommon = string[0]
    for s in string:
        if string.count(s) > string.count(mostCommon):
            mostCommon = s

    return mostCommon


if __name__ == '__main__':
    str1 = "abcdbde"
    print(most_common_character(str1))

    str2 = "exemplaryelementary"
    print(most_common_character(str2))
