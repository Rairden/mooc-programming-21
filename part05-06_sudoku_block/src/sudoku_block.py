def block_correct(sudoku: list, rowNo: int, colNo: int):
    WIDTH = 3
    matrix = []
    frequency = []

    for i in range(WIDTH):
        for k in range(WIDTH):
            matrix.append(sudoku[i + rowNo][k + colNo])

    for i in range(10):
        frequency.append(matrix.count(i))
    frequency = frequency[1:]

    return not any(num > 1 for num in frequency)


if __name__ == '__main__':
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))  # false
    print(block_correct(sudoku, 1, 2))  # true
