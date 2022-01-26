def line(num, str):
    for _ in range(0, num):
        if len(str) == 0:
            print("*", end="")
        else:
            print(str[0], end="")
    print()


def square(size, character):
    for _ in range(0, size):
        line(size, character)


if __name__ == "__main__":
    square(5, "x")
