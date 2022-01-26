arr = [1, 2, 3, 4, 5]

while True:
    idx = int(input("Index: "))
    if idx == -1:
        break

    val = int(input("New value: "))
    arr[idx] = val
    print(arr)
