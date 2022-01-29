def print_sudoku(sudoku: list):
    for i, e in enumerate(sudoku):
        if i == 3 or i == 6:
            print()

        for ii, ee in enumerate(e):
            if ii == 3 or ii == 6:
                print(" ", end="")
            if ee == 0:
                print("_ ", end="")
            else:
                print(f"{ee} ", end="")

        print()


def add_number(sudoku: list, rowNo: int, colNo: int, num:int):
    sudoku[rowNo][colNo] += num


if __name__ == '__main__':
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print("\nThree numbers added:\n")
    print_sudoku(sudoku)
