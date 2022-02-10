import string


def change_case(origStr: str):
    new = ""
    for s in origStr:
        if s.islower():
            new += s.upper()
            continue
        new += s.lower()

    return new


def split_in_half(origStr: str):
    length = len(origStr)
    half = length // 2

    s1 = origStr[:half]
    s2 = origStr[half:]
    return s1, s2


def remove_special_characters(origStr: str):
    legal = string.ascii_letters + string.digits + string.whitespace
    new = ""
    for s in origStr:
        if s in legal:
            new += s

    return new
