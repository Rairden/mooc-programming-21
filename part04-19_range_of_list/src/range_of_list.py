def range_of_list(arr: list):
    return max(arr) - min(arr)


if __name__ == "__main__":
    nums = [3, 6, -4]
    result = range_of_list(nums)
    print(result)
