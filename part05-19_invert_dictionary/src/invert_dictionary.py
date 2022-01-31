def invert(db: dict):
    copy = db.copy()

    for k in copy:
        val = copy[k]
        db[val] = k
        del db[k]


if __name__ == '__main__':
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
