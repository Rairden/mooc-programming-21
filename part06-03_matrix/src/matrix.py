def convertFileToMatrix(file):
    matrix = []
    with open(file) as file:
        for line in file:
            ln = line.split(",")
            row = list(map(int, ln))
            matrix.append(row)

    return matrix


def matrix_sum():
    matrix = convertFileToMatrix("matrix.txt")
    summation = 0
    for line in matrix:
        summation += sum(line)

    return summation


def matrix_max():
    matrix = convertFileToMatrix("matrix.txt")
    maximum = 0
    for line in matrix:
        maxVal = max(line)
        if maxVal > maximum:
            maximum = maxVal

    return maximum


def row_sums():
    matrix = convertFileToMatrix("matrix.txt")
    rowSums = []
    for line in matrix:
        summation = sum(line)
        rowSums.append(summation)

    return rowSums


if __name__ == '__main__':
    matrixSum = matrix_sum()
    matrixMax = matrix_max()
    matrixRowSums = row_sums()
    print(matrixSum)
    print(matrixMax)
    print(matrixRowSums)
