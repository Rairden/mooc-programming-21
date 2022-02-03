def fileToMap1(file1):
    with open(file1) as file:
        next(file)  # skip first line
        students = {}
        for line in file:
            ln = line.split(";")
            students[ln[0]] = (ln[1], ln[2].replace("\n", ""))

    return students


def fileToMap2(file2):
    with open(file2) as file:
        next(file)

        completed = {}
        for line in file:
            line = line.replace("\n", "").split(";")
            pts = line[1:]
            completed[line[0]] = pts

    return completed


def main():
    studentInfo = input("Student information: ")
    exerciseData = input("Exercises completed: ")

    students = fileToMap1(studentInfo)
    exercises = fileToMap2(exerciseData)

    for key, val in exercises.items():
        total = 0
        for v in val:
            total += int(v)

        student = students[key]
        fName = student[0]
        lName = student[1]
        print(fName, lName, total)


main()
