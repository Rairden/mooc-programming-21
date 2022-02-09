import difflib
import sys


def createSet(fileName):
    with open(fileName) as file:
        words = set()
        for line in file:
            ln = line.strip().split(" ")
            for word in ln:
                words.add(word)

    return words


file = "wordlist.txt"
wordSet = createSet(file)
inputText = input("Write text: ")

text = inputText.strip().split(" ")
misspelled = {}

for word in text:
    wordLower = word.lower()
    if wordLower not in wordSet:
        misspelled[wordLower] = []
        print(f"*{word}* ", end="")
    else:
        print(f"{word} ", end="")

if len(misspelled) == 0:
    sys.exit(0)

for word in misspelled:
    suggest = difflib.get_close_matches(word, wordSet)
    misspelled[word].extend(suggest)

print("\nsuggestions:")
for word, sugg in misspelled.items():
    suggestions = ", ".join(sugg)
    print(f"{word}: {suggestions}")
