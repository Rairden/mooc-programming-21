def anagrams(str1,  str2):
    s1 = sorted(str1)
    s2 = sorted(str2)

    return s1 == s2


if __name__ == '__main__':
    b = anagrams("erik", "kire")
    print(b)
