def even_numbers(nums: list):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    return evens


if __name__ == '__main__':
    a = [1, 2, -5, 60]
    print(even_numbers(a))
