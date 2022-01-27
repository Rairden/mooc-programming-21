def list_sum(a, b):
    sums = []
    for i in range(len(a)):
        sums.append(a[i] + b[i])
    return sums


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [7, 8, 9]
    add = list_sum(a, b)
    print(add)
