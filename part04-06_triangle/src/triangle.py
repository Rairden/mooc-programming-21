def line(num, str):
    for _ in range(0, num):
        if len(str) == 0:
            print("*", end="")
        else:
            print(str[0], end="")
    print()


def triangle(size):
    for i in range(1, size + 1):
        line(i, "#")


if __name__ == "__main__":
    triangle(5)
