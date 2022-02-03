def largest():
    with open("numbers.txt") as file:
        max = 0
        for line in file:
            num = int(line)
            if num > max:
                max = num

    return max


if __name__ == '__main__':
    largest()
