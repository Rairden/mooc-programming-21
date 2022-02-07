import os


def filter_solutions():
    os.remove("correct.csv")
    os.remove("incorrect.csv")

    with open("solutions.csv", "r") as file:
        for line in file:
            ln = line.split(";")
            expression = ln[1]
            result = int(ln[2])

            answer = eval(expression)

            if result == answer:
                with open("correct.csv", "a") as f:
                    f.write(line)
            else:
                with open("incorrect.csv", "a") as f:
                    f.write(line)


if __name__ == '__main__':
    filter_solutions()
