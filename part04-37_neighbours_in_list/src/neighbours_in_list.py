def longest_series_of_neighbours(nums: list):
    cnt = 1
    max = 1
    start = 0

    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) == 1:
            cnt += 1
            if cnt > max:
                max = cnt
                start = i - max + 1
        else:
            cnt = 1

    ans = nums[start:start + max]
    return len(ans)


if __name__ == '__main__':
    numbers = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(numbers))    # 4
    numbers2 = [1, 2, 3, 5, 6, 9, 10]
    print(longest_series_of_neighbours(numbers2))   # 3
    numbers3 = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(numbers3))   # 7
