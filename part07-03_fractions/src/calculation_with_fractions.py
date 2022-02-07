import fractions


def fractionate(amount: int):
    parts = []
    for i in range(amount):
        f = fractions.Fraction(1, amount)
        parts.append(f)

    return parts


if __name__ == '__main__':
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))
