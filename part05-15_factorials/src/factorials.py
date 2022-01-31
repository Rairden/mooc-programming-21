def factorials(n: int):
    factorial = {}
    sum = 1
    val = 1

    while val <= n:
        factorial[val] = sum
        val += 1
        sum *= val

    return factorial


if __name__ == '__main__':
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
