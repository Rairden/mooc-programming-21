def everything_reversed(strs: list):
    rev = []
    for s in strs[::-1]:
        rev.append(s[::-1])

    return rev


if __name__ == '__main__':
    strings = ["Hi", "there", "example", "one more"]
    revStrings = everything_reversed(strings)
    print(revStrings)
