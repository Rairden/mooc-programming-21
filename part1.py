from math import sqrt


def sevenBrothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")


def rowrow():
    msg = """Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream."""
    print(msg)


def minutesPerYear():
    minsPerDay = 60 * 24
    minsPerYear = minsPerDay * 365
    return minsPerYear


def printSomeCode():
    print('print("Hello there!")')


def nameTwice():
    name = input("What is your name? ")
    print(name)
    print(name)


def nameExclam():
    name = input("What is your name? ")
    print("!" + name + "!" + name + "!")


def nameAndAddress():
    nameFirst = input("Given name: ")
    nameLast = input("Family name: ")
    addr = input("Street address: ")
    city = input("City and postal code: ")

    # print("{} {}".format(nameFirst, nameLast))
    print(nameFirst + " " + nameLast)
    print(addr)
    print(city)


def utterances():
    p1 = input("The 1st part: ")
    p2 = input("The 2nd part: ")
    p3 = input("The 3rd part: ")
    # print(p1 + "-" + p2 + "-" + p3 + "!")
    print(f"{p1}-{p2}-{p3}!")


def story():
    name = input("Please type in a name: ")
    birthYear = input("Please type in a year: ")

    msg = f"""{name} is valiant knight, born in the year {birthYear}.
One morning {name} woke up to an awful racket: a dragon was approaching
the village. Only {name} could save the village's residents."""

    msg2 = (
        f"{name} is valiant knight, born in the year {birthYear}. "
        f"One morning {name} woke up to an awful racket: a dragon was approaching "
        f"the village. Only {name} could save the village's residents."
    )

    print(msg)
    print()
    print(msg2)


def extraSpace():
    name = "Tim Tester"
    age = 20
    skill1 = "python"
    level1 = "beginner"
    skill2 = "java"
    level2 = "veteran"
    skill3 = "programming"
    level3 = "semiprofessional"
    lower = 2000
    upper = 3000

    print(f"my name is {name}, I am {age} years old\n")
    print("my skills are")
    print(f" - {skill1} ({level1})")
    print(f" - {skill2} ({level2})")
    print(f" - {skill3} ({level3})\n")

    print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")


def arithmetics():
    x = 27
    y = 15
    print(f"{x} + {y} = " + str(x + y))
    print(f"{x} - {y} = " + str(x - y))
    print(f"{x} * {y} = " + str(x * y))
    print(f"{x} / {y} = " + str(x / y))


def printSingleLine():
    print(5, end="")
    print(" + ", end="")
    print(8, end="")
    print(" - ", end="")
    print(4, end="")
    print(" = ", end="")
    print(5 + 8 - 4)


def timesFive():
    num = input("Please type in a number: ")
    result = int(num) * 5
    print(f"{num} times 5 is {result}")


def nameAndAge():
    # Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
    name = input("What is your name? ")
    birthYear = input("Which year were you born? ")

    age = 2021 - int(birthYear)
    print(f"Hi {name}, you will be {age} years old at the end of the year 2021")


def secondsInADay():
    secondsPerDay = 60 * 60 * 24
    days = int(input("How many days? "))
    print(f"Seconds in that many days: {days * secondsPerDay}")


def product():
    number = int(input("Please type in the first number: "))
    number *= int(input("Please type in the second number: "))
    number *= int(input("Please type in the third number: "))

    print("The product is", number)


def sumAndProduct():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))

    print("The sum of the numbers:", num1 + num2)
    print("The product of the numbers:", num1 * num2)


def sumAndMean():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    num3 = int(input("Number 3: "))
    num4 = int(input("Number 4: "))
    summation = num1 + num2 + num3 + num4
    print(f"The sum of the numbers is {summation} and the mean is {summation / 4}")


def foodExpenditure():
    timesPerWeek = int(input("How many times a week do you eat at the student cafeteria? "))
    lunchPrice = float(input("The price of a typical student lunch? "))
    weeklyGrocery = float(input("How much money do you spend on groceries in a week? "))

    weeklyLunch = timesPerWeek * lunchPrice
    lunchAvg = weeklyLunch / 7
    grocAvg = weeklyGrocery / 7

    totalDaily = lunchAvg + grocAvg

    print("Average food expenditure:")
    print(f"Daily: {totalDaily} euros")
    print(f"Weekly: {totalDaily * 7} euros")


def studentsInGroups():
    numStudents = int(input("How many students on the course? "))
    groupSize = int(input("Desired group size? "))

    if numStudents % groupSize == 0:
        print("Number of groups formed: ", int(numStudents / groupSize))
    else:
        print("Number of groups formed: ", numStudents // groupSize + 1)


def orwell():
    num = input("Please type in a number: ")

    if num == "1984":
        print("Orwell")


def absoluteValue():
    num = abs(int(input("Please type in a number: ")))
    print(f"The absolute value of this number is {num}")


def soupOrNoSoup():
    name = input("Please tell me your name: ")

    if name != "Jerry":
        num = int(input("How many portions of soup? "))
        portionPrice = 5.90
        print(f"The total cost is {num * portionPrice}")

    print("Next please!")


def orderOfMagnitude():
    num = int(input("Please type in a number: "))

    if num < 1000:
        print("This number is smaller than 1000")
    if num < 100:
        print("This number is smaller than 100")
    if num < 10:
        print("This number is smaller than 10")

    print("Thank you!")


def calculator():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    op = input("Operation: ")

    if op == "add":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "subtract":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "multiply":
        print(f"{num1} * {num2} = {num1 * num2}")


def temperature():
    tempF = int(input("Please type in a temperature (F): "))
    tempC = (tempF - 32) * (5 / 9)

    print(f"{tempF} degrees Fahrenheit equals {tempC} degrees Celsius")

    if tempC < 0:
        print("Brr! It's cold in here!")


def dailyWages():
    hourlyWage = float(input("Hourly wage: "))
    hours = float(input("Hours worked: "))
    day = input("Day of week: ")

    if day == "Sunday":
        print(f"Daily wages: {hourlyWage * 2 * hours} euros")
    else:
        print(f"Daily wages: {hourlyWage * hours} euros")


def loyaltyBonus():
    points = int(input("How many points are on your card? "))
    if points < 100:
        points *= 1.1
        print("Your bonus is 10 %")
    else:
        points *= 1.15
        print("Your bonus is 15 %")

    print("You now have", points, "points")


def whatToWear():
    print("What is the weather forecast for tomorrow?")
    celsius = int(input("Temperature: "))
    raining = input("Will it rain (yes/no): ")

    print("Wear jeans and a T-shirt")

    if celsius <= 20:
        print("I recommend a jumper as well")
    if celsius <= 10:
        print("Take a jacket with you")
    if celsius <= 5:
        print("Make it a warm coat, actually\n"
              "I think gloves are in order")

    if raining == "yes":
        print("Don't forget your umbrella!")


def quadratic():
    a = float(input("Value of a: "))
    b = float(input("Value of b: "))
    c = float(input("Value of c: "))

    # eqn is x = (-b ± sqrt(b²-4ac))/(2a).
    result1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    result2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    print(f"The roots are {result1} and {result2}")


quadratic()
# whatToWear()
# loyaltyBonus()
# dailyWages()
# temperature()
# calculator()
# orderOfMagnitude()
# soupOrNoSoup()
# absoluteValue()
# orwell()
# studentsInGroups()
# foodExpenditure()
# sumAndMean()
# sumAndProduct()
# product()
# secondsInADay()
# nameAndAge()
# timesFive()
# printSingleLine()
# arithmetics()
# extraSpace()
# story()
# utterances()
# nameAndAddress()
# nameExclam()
# nameTwice()
# printSomeCode()
# print(minutesPerYear())
# rowrow()
# sevenBrothers()
