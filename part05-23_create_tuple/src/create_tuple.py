def create_tuple(x: int, y: int, z: int):
    min1 = min(x, y, z)
    max1 = max(x, y, z)

    tup = (min1, max1, x + y + z)
    return tup


if __name__ == '__main__':
    print(create_tuple(5, 3, -1))
