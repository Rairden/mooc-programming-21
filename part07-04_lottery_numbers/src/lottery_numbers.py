from random import sample


def lottery_numbers(amount: int, lower: int, upper: int):
    numberPool = list(range(lower, upper))
    chosenNums = sample(numberPool, amount)
    return sorted(chosenNums)


if __name__ == '__main__':
    for number in lottery_numbers(7, 1, 40):
        print(number)
