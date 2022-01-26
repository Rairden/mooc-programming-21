def same_chars(str, i, k):
    if i < len(str) and k < len(str):
        return str[i] == str[k]
    return False


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
