import string
from random import choice


def generate_strong_password(length: int, hasDigits: bool, hasSpecial: bool):
    letters = string.ascii_lowercase
    digits = string.digits
    alphaNum = letters + digits
    special = "!?=+-()#"
    allChars = alphaNum + special
    passwd = ""

    for i in range(length):
        if not hasDigits and not hasSpecial:
            passwd += choice(letters)
        elif hasDigits and not hasSpecial:
            passwd += choice(alphaNum)
            if digits not in passwd:
                passwd = passwd[1:] + "5"
        elif not hasDigits and hasSpecial:
            passwd += choice(letters + special)
            if special not in passwd:
                passwd = passwd[1:] + "#"
        elif hasDigits and hasSpecial:
            passwd += choice(allChars)
            if digits not in passwd:
                passwd = passwd[1:] + "5"
            if special not in passwd:
                passwd = passwd[1:] + "("

    return passwd


if __name__ == '__main__':
    for i in range(10):
        print(generate_strong_password(8, True, True))
