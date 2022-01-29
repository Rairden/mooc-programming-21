def play_turn(gameBoard: list, x: int, y: int, piece: str):
    if not 0 <= x <= 2 or not 0 <= y <= 2:
        return False

    move = "XO"
    mark = gameBoard[y][x]

    if mark in move and mark != "":
        return False

    gameBoard[y][x] = piece
    return True


if __name__ == '__main__':
    gameBoard = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(gameBoard, 2, 0, "X"))
    print(gameBoard)

    gameBoard2 = [['X', 'X', ''], ['', 'O', 'X'], ['', '', 'O']]
    print(play_turn(gameBoard2, 0, 0, "X"))
    print(gameBoard2)

    gameBoard3 = [['', '', 'O'], ['', '', ''], ['', 'X', 'O']]
    print(play_turn(gameBoard3, 3, 0, "X"))
    print(gameBoard3)
