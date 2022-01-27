def distinct_numbers(nums):
    new = []
    for n in nums:
        if n not in new:
            new.append(n)

    return sorted(new)


if __name__ == '__main__':
    nums = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(nums))  # [1, 2, 3]
