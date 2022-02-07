from random import shuffle


def words(n: int, beginning: str):
    words = []
    matches = []

    with open("words.txt", "r") as file:
        for line in file:
            word = line.replace("\n", "")
            words.append(word)

    for w in words:
        if w.startswith(beginning):
            matches.append(w)

    if len(matches) < n:
        raise ValueError(f"Not enough words. Result size: {len(matches)}")

    shuffle(matches)
    return matches[:n]


if __name__ == '__main__':
    wordList = words(3, "ca")
    for word in wordList:
        print(word)
