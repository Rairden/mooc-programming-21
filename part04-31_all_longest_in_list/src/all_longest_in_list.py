def all_the_longest(str: list):
    result = [""]
    for s in str:
        if len(s) > len(result[0]):
            result = [s]
        elif len(s) == len(result[0]):
            result.append(s)

    return result


if __name__ == '__main__':
    names = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    names2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard", "rairden"]
    names3 = ["dorothy", "richard", "rairden"]
    names4 = ['Alan', 'Steve', 'Seymour', 'Kim', 'Susan']

    print(all_the_longest(names))   # ['dorothy', 'richard']
    print(all_the_longest(names2))  # ['dorothy', 'richard', 'rairden']
    print(all_the_longest(names3))  # ['dorothy', 'richard', 'rairden']
    print(all_the_longest(names4))  # ['Seymour']
