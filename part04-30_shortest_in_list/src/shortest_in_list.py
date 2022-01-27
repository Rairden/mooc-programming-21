def shortest(strings: list):
    shortest = strings[0]
    for s in strings:
        if len(s) < len(shortest):
            shortest = s

    return shortest


if __name__ == '__main__':
    names = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(names)
    print(result)
