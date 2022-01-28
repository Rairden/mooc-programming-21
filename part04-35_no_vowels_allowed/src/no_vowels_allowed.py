def no_vowels(string):
    for s in string:
        if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
            string = string.replace(s, "")

    return string


if __name__ == '__main__':
    str1 = "this is an example"
    print(no_vowels(str1))
