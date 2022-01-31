def times_ten(start: int, end: int):
    dict = {}
    for i in range(start, end + 1):
        dict[i] = i * 10

    return dict


if __name__ == '__main__':
    d = times_ten(3, 6)
    print(d)
