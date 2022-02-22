class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, arr: list):
        num = 0
        counter = 0

        for i in arr:
            freq = arr.count(i)
            if freq > counter:
                counter = freq
                num = i

        return num

    @classmethod
    def doubles(cls, arr: list):
        cnt = 0
        mySet = set(arr)
        for a in mySet:
            if arr.count(a) > 1:
                cnt += 1

        return cnt


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(nums))
    print(ListHelper.doubles(nums))
