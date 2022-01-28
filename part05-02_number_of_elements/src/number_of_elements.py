def count_matching_elements(matrix: list, elem: int):
    cnt = 0
    for m in matrix:
        for n in m:
            if n == elem:
                cnt += 1
    return cnt


if __name__ == '__main__':
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
