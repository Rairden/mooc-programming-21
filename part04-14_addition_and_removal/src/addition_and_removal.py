nums = []
print("The list is now", nums)

while True:
    op = input("a(d)d, (r)emove or e(x)it: ")

    if op == 'd':
        nums.append(len(nums) + 1)
        print("The list is now", nums)
    elif op == 'r':
        nums.pop()
        print("The list is now", nums)
    elif op == 'x':
        print("Bye!")
        break
