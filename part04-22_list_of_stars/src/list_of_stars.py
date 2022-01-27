def list_of_stars(nums: list):
    for n in nums:
        print("*" * n)


if __name__ == '__main__':
    arr = [3, 7, 1, 1, 2]
    list_of_stars(arr)
