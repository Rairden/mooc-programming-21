def line(num, str):
    for _ in range(num):
        print(str[0], end="")
    print()


def histogram(str):
    freq = {}
    for s in str:
        if s not in freq:
            freq[s] = str.count(s)

    for s in freq:
        print(f"{s} ", end="")
        line(freq[s], "*")


if __name__ == '__main__':
    histogram("statistically")
