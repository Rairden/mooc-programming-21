def read_fruits():
    fruits = {}

    with open("fruits.csv") as file:
        for line in file:
            a, b = line.split(";")
            fruit = a
            price = float(b)
            fruits[fruit] = price

    return fruits


if __name__ == '__main__':
    read_fruits()
