from random import choice


def roll(die: str):
    """
    Die A has the sides 3, 3, 3, 3, 3, 6
    Die B has the sides 2, 2, 2, 5, 5, 5
    Die C has the sides 1, 4, 4, 4, 4, 4
    """
    A = "333336"
    B = "222555"
    C = "144444"

    char = ""
    if die == "A":
        char = choice(A)
    elif die == "B":
        char = choice(B)
    elif die == "C":
        char = choice(C)

    return int(char)


def play(die1: str, die2: str, times: int):
    die1Wins = 0
    die2Wins = 0
    ties = 0
    for i in range(times):
        die1Roll = roll(die1)
        die2Roll = roll(die2)

        if die1Roll > die2Roll:
            die1Wins += 1
        elif die2Roll > die1Roll:
            die2Wins += 1
        else:
            ties += 1

    return die1Wins, die2Wins, ties


if __name__ == '__main__':
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
