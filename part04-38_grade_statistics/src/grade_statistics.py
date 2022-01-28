def printGradeDistributions(num, str):
    for _ in range(num):
        print(str[0], end="")
    print()


def printStatistics(students, pts, summary):
    print("Statistics:")
    print("Points average:", pts / students)
    avgPass = (gradeOne + gradeTwo + gradeThree + gradeFour + gradeFive) / students * 100
    print(f"Pass percentage: {avgPass:.1f}")
    print("Grade distribution: ")

    for i, k in reversed(list(enumerate(summary))):
        print(f"  {i}: ", end="")
        printGradeDistributions(k, "*")


gradeZero = 0
sumStudentPts = numStudents = gradeOne = gradeTwo = gradeThree = gradeFour = gradeFive = gradeZero

while True:
    line = input("Exam points and exercises completed: ")

    if line == "":
        gradeSummary = [gradeZero, gradeOne, gradeTwo, gradeThree, gradeFour, gradeFive]
        printStatistics(numStudents, sumStudentPts, gradeSummary)
        break

    split = line.split(" ")
    examScore = int(split[0])
    exercises = int(split[1])

    numStudents += 1
    exercisePts = int(exercises * 0.1)
    totalStudentPts = examScore + exercisePts
    sumStudentPts += totalStudentPts

    if examScore < 10:
        gradeZero += 1
        continue

    if 0 <= totalStudentPts <= 14:
        gradeZero += 1
    elif 15 <= totalStudentPts <= 17:
        gradeOne += 1
    elif 18 <= totalStudentPts <= 20:
        gradeTwo += 1
    elif 21 <= totalStudentPts <= 23:
        gradeThree += 1
    elif 24 <= totalStudentPts <= 27:
        gradeFour += 1
    elif 28 <= totalStudentPts <= 30:
        gradeFive += 1
