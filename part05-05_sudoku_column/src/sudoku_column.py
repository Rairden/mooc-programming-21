def column_correct(sudoku: list, colNo: int):
    col = []
    frequency = []

    for row in sudoku:
        col.append(row[colNo])

    for i in range(len(col) + 1):
        frequency.append(col.count(i))
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

    print(column_correct(sudoku, 0))  # false
