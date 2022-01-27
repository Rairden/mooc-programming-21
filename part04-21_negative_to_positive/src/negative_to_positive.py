num = int(input("Please type in a positive integer: "))
low = num * -1

for i in range(low, num + 1):
    if i == 0:
        continue
    print(i)
