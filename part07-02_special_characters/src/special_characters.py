import string


def separate_characters(myString: str):
    ASCII = ""
    punctuation = ""
    others = ""

    for s in myString:
        if s in string.ascii_letters:
            ASCII += s
        elif s in string.punctuation:
            punctuation += s
        else:
            others += s

    return ASCII, punctuation, others


if __name__ == '__main__':
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
