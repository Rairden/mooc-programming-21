def remove_smallest(numbers: list):
    smallestIdx = 0
    smallest = numbers[0]

    for i, num in enumerate(numbers):
        if num < smallest:
            smallest = num
            smallestIdx = i

    numbers.pop(smallestIdx)


if __name__ == '__main__':
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)

    numbers2 = [1, 2, 3, 5, 6]
    remove_smallest(numbers2)
    print(numbers2)

    numbers3 = [9, 7, 5, 3]
    remove_smallest(numbers3)
    print(numbers3)
