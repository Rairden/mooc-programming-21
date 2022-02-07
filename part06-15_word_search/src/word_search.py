import re


def find_words(search: str):
    words = []
    matches = []

    with open("words.txt", "r") as f:
        for line in f:
            words.append(line.replace("\n", ""))

    if "*" in search:
        if search[0] == "*":
            for w in words:
                w.endswith(search[1:]) and matches.append(w)

            return matches

        for w in words:
            w.startswith(search[:-1]) and matches.append(w)
    elif "." in search:
        search = f"^{search}$"
        regex = re.compile(search)
        for w in words:
            regex.match(w) and matches.append(w)
    else:
        if search in words:
            matches.append(search)

    return matches


if __name__ == '__main__':
    words1 = find_words("ca.")
    words2 = find_words("reson*")
