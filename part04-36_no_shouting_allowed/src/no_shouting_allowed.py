def no_shouting(strings: list):
    pruned = []
    for s in strings:
        if not s.isupper():
            pruned.append(s)

    return pruned


if __name__ == '__main__':
    words = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    filtered = no_shouting(words)
    print(filtered)
