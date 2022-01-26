items = []
size = int(input("How many items: "))

for i in range(0, size):
    item = int(input(f"Item {i + 1}: "))
    items.append(item)

print(items)
