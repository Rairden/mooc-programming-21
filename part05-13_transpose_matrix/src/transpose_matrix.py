from copy import deepcopy


def transpose(matrix: list):
    copy = deepcopy(matrix)
    n = len(matrix)
    for i in range(n):
        for k in range(n):
            matrix[k][i] = copy[i][k]


def testMatrix1():
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transpose(mat)
    print(mat)


def testMatrix2():
    mat = [
        [1, 2],
        [1, 2]
    ]

    transpose(mat)
    print(mat)


def testMatrix3():
    mat = [
        [10, 100],
        [10, 100]
    ]

    transpose(mat)
    print(mat)


if __name__ == '__main__':
    testMatrix1()
