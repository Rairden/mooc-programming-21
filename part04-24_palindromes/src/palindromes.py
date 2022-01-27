def palindromes(str):
    rev = str[::-1]
    return str == rev


while True:
    word = input("Please type in a palindrome: ")

    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
