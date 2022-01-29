from copy import deepcopy

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


def copy_and_add(sudoku: list, row: int, col: int, num: int):
    copy = deepcopy(sudoku)
    copy[row][col] = num
    return copy


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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
