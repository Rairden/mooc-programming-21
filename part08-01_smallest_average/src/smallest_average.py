from statistics import mean


def smallest_average(p1: dict, p2: dict, p3: dict):
    p1vals = list(p1.values())[1:]
    smallest = mean(p1vals)
    answer = p1

    p2Vals = list(p2.values())[1:]
    p2vals = mean(p2Vals)
    if p2vals < smallest:
        smallest = p2vals
        answer = p2

    p3vals = list(p3.values())[1:]
    p3vals = mean(p3vals)
    if p3vals < smallest:
        answer = p3

    return answer


if __name__ == '__main__':
    p1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    p2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    p3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    smallestAvg = smallest_average(p1, p2, p3)
    print(smallestAvg)
