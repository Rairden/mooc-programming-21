def double_items(numbers: list):
    arr = []
    for n in numbers:
        arr.append(n * 2)

    return arr


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numsDoubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numsDoubled)
