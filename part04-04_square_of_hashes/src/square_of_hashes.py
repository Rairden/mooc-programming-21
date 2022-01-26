def line(num, str):
    for _ in range(0, num):
        if len(str) == 0:
            print("*", end="")
        else:
            print(str[0], end="")
    print()


def square_of_hashes(size):
    for i in range(0, size):
        line(size, "#")


if __name__ == "__main__":
    square_of_hashes(5)
