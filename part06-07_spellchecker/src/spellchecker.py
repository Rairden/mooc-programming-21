def createSet(fileName):
    with open(fileName) as file:
        words = set()
        for line in file:
            ln = line.replace("\n", "").split(" ")
            for word in ln:
                words.add(word)

    return words


def main():
    file = "wordlist.txt"
    wordSet = createSet(file)
    inputText = input("Write text: ")

    text = inputText.replace("\n", "").split(" ")

    for word in text:
        wordLower = word.lower()
        if wordLower not in wordSet:
            print(f"*{word}* ", end="")
        else:
            print(f"{word} ", end="")


main()
