def spruce(height):
    if height > 0:
        print("a spruce!")

    k = 1
    for i in range(1, height + 1):
        print(" " * (height - i), end="")
        print("*" * k)
        k += 2
    print(" " * (height - 1) + "*")


if __name__ == "__main__":
    spruce(3)
