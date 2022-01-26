words = []

while True:
    str = input("Word: ")

    if str in words:
        print(f"You typed in {len(words)} different words")
        break

    words.append(str)
