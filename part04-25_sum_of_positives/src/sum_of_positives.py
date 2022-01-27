def sum_of_positives(nums: list):
    sum = 0
    for e in nums:
        if e > 0:
            sum += e

    return sum


if __name__ == '__main__':
    a = [1, 2, -5, 60]
    print(sum_of_positives(a))
