def mean(arr: list):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    nums = [3, 6, -4]
    result = mean(nums)
    print(result)
