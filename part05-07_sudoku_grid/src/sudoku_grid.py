def row_correct(sudoku: list, rowNo: int):
    row = sudoku[rowNo]
    frequency = []

    for i in range(len(row) + 1):
        frequency.append(row.count(i))

    frequency = frequency[1:]
    return not any(num > 1 for num in frequency)


def column_correct(sudoku: list, colNo: int):
    col = []
    frequency = []

    for row in sudoku:
        col.append(row[colNo])

    for i in range(len(col) + 1):
        frequency.append(col.count(i))
    frequency = frequency[1:]

    return not any(num > 1 for num in frequency)


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


def sudoku_grid_correct(sudoku: list):
    """
    Check all rows, columns and also the 3x3 subgrids:
    (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6)
    """
    subGridsCorrect = False
    if (block_correct(sudoku, 0, 0) and
        block_correct(sudoku, 0, 3) and
        block_correct(sudoku, 0, 6) and
        block_correct(sudoku, 3, 0) and
        block_correct(sudoku, 3, 3) and
        block_correct(sudoku, 3, 6) and
        block_correct(sudoku, 6, 0) and
        block_correct(sudoku, 6, 3) and
        block_correct(sudoku, 6, 6)):
        subGridsCorrect = True

    for i in range(len(sudoku)):
        rowCorrect = row_correct(sudoku, i)
        colCorrect = column_correct(sudoku, i)

        if not rowCorrect or not colCorrect:
            return False

    return subGridsCorrect


if __name__ == '__main__':
    sudoku1 = [
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

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    sudoku3 = [
        [6, 4, 9, 2, 8, 3, 1, 5, 7],
        [0, 5, 0, 6, 4, 9, 2, 3, 8],
        [2, 3, 8, 1, 5, 7, 6, 4, 9],
        [9, 2, 3, 8, 1, 5, 0, 6, 4],
        [7, 6, 4, 9, 2, 3, 8, 1, 5],
        [8, 1, 5, 7, 0, 4, 9, 2, 0],
        [5, 7, 6, 4, 9, 2, 3, 2, 1],
        [4, 0, 2, 3, 8, 1, 5, 0, 6],
        [3, 0, 1, 5, 0, 6, 4, 9, 0],
    ]

    print(sudoku_grid_correct(sudoku1)) # false
    print(sudoku_grid_correct(sudoku2)) # true
    print(sudoku_grid_correct(sudoku3)) # false
