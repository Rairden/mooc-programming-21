def print_student(students: dict, name):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    if len(students[name]) == 0:
        print(f"{name}:\n no completed courses")
        return

    courses = students[name]
    totalCourses = len(courses)
    avgGrade = 0
    sum = 0

    print(f"{name}:\n {totalCourses} completed courses:")

    for course, grade in courses.items():
        sum += grade[1]
        print(f"  {course} {grade[1]}")

    print(" average grade", sum / totalCourses)


def add_student(students: dict, name):
    students[name] = {}


def add_course(students: dict, name, completed: tuple):
    if completed[1] == 0:
        return

    completedCourses = students[name]
    course = completed[0]
    grade = completed[1]

    if course in completedCourses:
        if completedCourses[course][1] > grade:
            return

    completedCourses[course] = completed


def summary(students: dict):
    """Duplicate courses don't affect the number of "completed courses",
    the avg or "best avg grade".
    """
    print("students", len(students))

    mostCourses = 0
    mostCompleted = ""

    highestAvg = 0
    bestStudent = ""

    for key, courses in students.items():
        gradeSum = 0
        numCourses = len(courses)
        for c in courses:
            gradeSum += courses[c][1]

        if numCourses > mostCourses:
            mostCourses = numCourses
            mostCompleted = key

        avg = gradeSum / numCourses
        if avg > highestAvg:
            highestAvg = avg
            bestStudent = key

    print(f"most courses completed", mostCourses, mostCompleted)
    print(f"best average grade", highestAvg, bestStudent)


def test1():
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")
    print()


def test2():
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
    print()


def test3():
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")
    print()


def test4():
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Introduction to Programming", 5))
    add_course(students, "Emily", ("Introduction to Databases", 4))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    print_student(students, "Emily")
    print()


def test5():
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)


if __name__ == '__main__':
    test1()
    # test2()
    # test3()
    # test4()
    # test5()
