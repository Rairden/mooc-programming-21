def line(num, str):
    for _ in range(0, num):
        if len(str) == 0:
            print("*", end="")
        else:
            print(str[0], end="")
    print()


def triangle(size, char):
    for i in range(1, size + 1):
        line(i, char)


def shape(width, char1, height, char2):
    triangle(width, char1)
    for i in range(0, height):
        line(width, char2)


if __name__ == "__main__":
    shape(5, "x", 2, "o")
