def formatted(numbers: list):
    result = []
    for n in numbers:
        result.append(f"{n:.2f}")

    return result


if __name__ == '__main__':
    nums = [1.234, 0.3333, 0.11111, 3.446]
    nums2 = formatted(nums)
    print(nums2)
