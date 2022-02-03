def csvToMap1(file1):
    with open(file1) as file:
        next(file)  # skip first line

        students = {}
        for line in file:
            ln = line.split(";")
            students[ln[0]] = (ln[1], ln[2].replace("\n", ""))

    return students


def csvToMap2(file1):
    with open(file1) as file:
        next(file)  # skip first line

        completed = {}
        for line in file:
            line = line.replace("\n", "").split(";")
            pts = line[1:]
            completed[line[0]] = pts

    return completed


def convertExercisePts(pts):
    # Completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc.
    # Completing all 40 exercises awards 10 points.

    totalPossible = 40
    pts /= totalPossible
    return int(pts * 10)


def sumPoints(nums: list):
    total = 0
    for n in nums:
        total += int(n)
    return total


def calcGrade(p):
    if p <= 14:
        return 0
    elif 15 <= p <= 17:
        return 1
    elif 18 <= p <= 20:
        return 2
    elif 21 <= p <= 23:
        return 3
    elif 24 <= p <= 27:
        return 4
    elif p >= 28:
        return 5


def main():
    studentInfo = input("Student information: ")
    exerciseData = input("Exercises completed: ")
    examsData = input("Exam points: ")

    students = csvToMap1(studentInfo)
    exercises = csvToMap2(exerciseData)
    exams = csvToMap2(examsData)

    for s in students:
        exercisePts = sumPoints(exercises[s])
        exercisePts = convertExercisePts(exercisePts)
        examPts = sumPoints(exams[s])
        totalPts = exercisePts + examPts

        # grade = exam pts + exercise pts
        grade = calcGrade(totalPts)
        student = students[s]
        fName = students[s][0]
        lName = students[s][1]
        print(fName, lName, grade)


main()
