def length_of_longest(strings: list):
    longest = 0
    for s in strings:
        if len(s) > longest:
            longest = len(s)

    return longest


if __name__ == '__main__':
    names = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(names)
    print(result)
