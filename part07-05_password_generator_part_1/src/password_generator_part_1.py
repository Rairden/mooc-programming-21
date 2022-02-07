from random import randint


def generate_password(length: int):
    passWord = ""
    for i in range(length):
        randomAscii = chr(randint(97, 122))
        passWord += randomAscii

    return passWord


if __name__ == '__main__':
    for i in range(10):
        print(generate_password(8))
