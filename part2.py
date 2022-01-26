from math import sqrt


def fixSyntax():
    number = int(input("Please type in a number: "))
    if number > 100:
        print("The number was greater than one hundred")
        number -= 100
        print("Now its value has decreased by one hundred")
        print("Its value is now", number)

    print(f"{number} must be my lucky number!")
    print("Have a nice day!")


def numberOfChars():
    word = input("Please type in a word: ")
    length = len(word)

    if length > 1:
        print(f"There are {length} letters in the word {word}")

    print("Thank you!")


def typecasting():
    num = float(input("Please type in a number: "))
    integral = int(num)

    print(f"Integer part: {integral}")
    print(f"Decimal part: {num - integral}")


def age():
    age = int(input("How old are you?: "))
    if age >= 18:
        print("You are of age!")
    else:
        print("You are not of age!")


def greaterThan():
    num1 = int(input("Please type in the first number: "))
    num2 = int(input("Please type in another number: "))

    if num1 == num2:
        print("The numbers are equal")
        return
    if num1 > num2:
        print("The greater number was:", num1)
    else:
        print("The greater number was:", num2)


def theElder():
    print("Person 1:")
    name1 = input("Name: ")
    age1 = int(input("Age: "))

    print("Person 2:")
    name2 = input("Name: ")
    age2 = int(input("Age: "))

    if age1 == age2:
        print(f"{name1} and {name2} are the same age")
        return

    if age1 > age2:
        print(f"The elder is {name1}")
    else:
        print(f"The elder is {name2}")


def alphabeticallyLast():
    word1 = input("Please type in the 1st word: ")
    word2 = input("Please type in the 2nd word: ")

    if word1 == word2:
        print("You gave the same word twice.")
        return

    if word1 > word2:
        print(f"{word1} comes alphabetically last.")
    else:
        print(f"{word2} comes alphabetically last.")


def ageCheck():
    age = int(input("What is your age? "))

    if age < 0:
        print("That must be a mistake")
        return

    if age < 5:
        print("I suspect you can't write quite yet...")
    else:
        print(f"Ok, you're {age} years old")


def nephews():
    name = input("Please type in your name: ")

    if name == "Ferdie" or name == "Morty":
        print("I think you might be one of Mickey Mouse's nephews.")
    elif name == "Louie" or name == "Dewey" or name == "Huey":
        print("I think you might be one of Donald Duck's nephews.")
    else:
        print("You're not a nephew of any character I know of.")


def gradesAndPoints():
    grade = int(input("How many points [0-100]: "))

    if grade < 0 or grade > 100:
        print("Grade: impossible!")
        return

    if 90 <= grade <= 100:
        print("Grade:", 5)
    elif 80 <= grade <= 90:
        print("Grade:", 4)
    elif 70 <= grade <= 80:
        print("Grade:", 3)
    elif 60 <= grade <= 70:
        print("Grade:", 2)
    elif 50 <= grade <= 60:
        print("Grade:", 1)
    elif grade < 50:
        print("Grade: fail")


def fizzbuzz():
    num = int(input("Number: "))

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")


def leapyear():
    year = int(input("Please type in a year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That year is a leap year.")
            else:
                print("That year is not a leap year.")
            return
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")


def isLeapYear(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False


# bubble sort algo
def alphabeticallyMiddle():
    a = input("1st letter: ")
    b = input("2nd letter: ")
    c = input("3rd letter: ")

    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    print("The letter in the middle is", b)


def taxCalc():
    gift = int(input("Value of gift: "))
    tax = 0

    if gift < 5000:
        print("No tax!")
        return

    if 5e3 <= gift <= 25e3:
        tax = 100 + (gift - 5e3) * 0.08
    elif 25e3 <= gift <= 55e3:
        tax = 1700 + (gift - 25e3) * 0.10
    elif 55e3 <= gift <= 200e3:
        tax = 4700 + (gift - 55e3) * 0.12
    elif 200e3 <= gift <= 1e6:
        tax = 22100 + (gift - 200e3) * 0.15
    elif gift > 1e6:
        tax = 142100 + (gift - 1e6) * .17

    print("Amount of tax:", tax)


def shallWeContinue():
    while True:
        print("hi")
        word = input("Shall we continue? ")
        if word == "no":
            print("okay then")
            break


def inputValidation():
    while True:
        num = float(input("Please type in a number: "))
        if num == 0:
            print("Exiting...")
            break

        if num < 0:
            print("Invalid number")
            continue

        print(sqrt(num))


def countdown():
    number = 5
    print("Countdown!")
    while True:
        print(number)
        number -= 1
        if number == 0:
            break

    print("Now!")


def repeatPassword():
    pass1 = input("Password: ")

    while True:
        pass2 = input("Repeat password: ")

        if pass1 == pass2:
            print("User account created!")
            break

        print("They do not match!")


def PIN():
    tries = 0

    while True:
        pin = input("PIN: ")
        if pin == "4321":
            tries += 1
            break

        if pin != "4321":
            print("Wrong")
            tries += 1
            continue

    if tries == 1:
        print("Correct! It only took you one single attempt!")
    else:
        print(f"Correct! It took you {tries} attempts")


def nextLeapYear():
    year = int(input("Year: "))
    nextLeap = year + 1

    while True:
        if isLeapYear(nextLeap):
            print(f"The next leap year after {year} is {nextLeap}")
            break

        nextLeap += 1


def story2():
    sentence = ""
    prev = ""

    while True:
        word = input("Please type in a word: ")
        if word == "end" or word == prev:
            print(sentence)
            break

        prev = word
        sentence += word + " "


def workingWithNumbers():
    print("Please type in integer numbers. Type in 0 to finish.")
    entries, sum, = 0, 0
    pos, neg = 0, 0

    while True:
        num = int(input("Number: "))
        sum += num
        entries += 1

        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1

        if num == 0:
            entries -= 1
            break

    print("... the program asks for numbers")
    print("Numbers typed in", entries)
    print("The sum of the numbers is", sum)
    print("The mean of the numbers is", sum / entries)
    print("Positive numbers", pos)
    print("Negative numbers", neg)


workingWithNumbers()


# story2()
# nextLeapYear()
# PIN()
# repeatPassword()
# countdown()
# inputValidation()
# shallWeContinue()
# taxCalc()
# alphabeticallyMiddle()
# leapyear()
# fizzbuzz()
# gradesAndPoints()
# nephews()
# ageCheck()
# alphabeticallyLast()
# theElder()
# greaterThan()
# age()
# typecasting()
# numberOfChars()
# fixSyntax()


def template():
    word = input("Please type in your name: ")
    pass

# template()
