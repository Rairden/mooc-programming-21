def all_the_longest(str: list):
    longestStr = 0
    longest = []

    for i, name in enumerate(str):
        if len(name) >= longestStr:
            longestStr = len(name)
            longest.append(i)

    res = []
    for i in range(len(longest) - 1):
        if len(str[longest[i]]) >= len(str[longest[i + 1]]):
            res.append(str[longest[i]])

    if len(str[longest[-1]]) >= len(str[longest[0]]):
        res.append(str[longest[-1]])

    for i in range(len(res) - 1):
        if len(res[i]) < len(res[i + 1]):
            res = res[i + 1:]

    return res


if __name__ == '__main__':
    names = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    names2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard", "rairden"]
    names3 = ["dorothy", "richard", "rairden"]
    names4 = ['Alan', 'Steve', 'Seymour', 'Kim', 'Susan']

    print(all_the_longest(names))   # ['dorothy', 'richard']
    print(all_the_longest(names2))  # ['dorothy', 'richard', 'rairden']
    print(all_the_longest(names3))  # ['dorothy', 'richard', 'rairden']
    print(all_the_longest(names4))  # ['Seymour']
