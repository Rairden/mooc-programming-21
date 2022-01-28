def row_correct(sudoku: list, rowNo: int):
    row = sudoku[rowNo]
    frequency = []

    for i in range(len(row) + 1):
        frequency.append(row.count(i))

    frequency = frequency[1:]
    return not any(num > 1 for num in frequency)


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
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 2, 0, 0, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 4, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 6, 6],
        [3, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 2, 0, 2, 0, 1],
    ]

    print(row_correct(sudoku1, 0))  # true
    print(row_correct(sudoku1, 1))  # false
    print(row_correct(sudoku2, 0))  # true
    print(row_correct(sudoku2, 1))  # false
