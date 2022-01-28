def who_won(gameBoard: list):
    ones, twos = 0, 0
    for r in gameBoard:
        ones += r.count((1))
        twos += r.count((2))

    if ones > twos:
        return 1
    if twos > ones:
        return 2

    return 0


if __name__ == '__main__':
    matrix1 = [
        [1, 2, 1],
        [0, 0, 1],
        [2, 1, 0]
    ]

    matrix2 = [
        [1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 2, 1],
        [2, 0, 2, 1, 1, 2],
        [1, 0, 0, 0, 1, 1],
        [1, 2, 0, 2, 1, 1]
    ]

    print(who_won(matrix1))
    print(who_won(matrix2))
