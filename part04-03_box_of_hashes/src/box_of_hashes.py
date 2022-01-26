def line(num, str):
    for _ in range(0, num):
        if len(str) == 0:
            print("*", end="")
        else:
            print(str[0], end="")


def box_of_hashes(height):
    for i in range(0, height):
        line(10, "#")
        print()


if __name__ == "__main__":
    box_of_hashes(5)
