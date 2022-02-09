import json
import urllib.request


def retrieve_all():
    response = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    courses = json.load(response)
    activeCourses = []
    for course in courses:
        if course["enabled"]:
            totalExercises = sum(course["exercises"])
            fullName = course["fullName"]
            year = course["year"]
            name = course["name"]
            entry = (fullName, name, year, totalExercises)
            activeCourses.append(entry)

    return activeCourses


def retrieve_course(course: str):
    """endpoint at https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats"""

    endpoint = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course}/stats"
    response = urllib.request.urlopen(endpoint)
    entries = json.load(response)

    weeks = len(entries)
    numStudents = []
    hours = []
    exercises = []
    for _, entry in entries.items():
        numStudents.append(entry["students"])
        hours.append(entry["hour_total"])
        exercises.append(entry["exercise_total"])

    result = {}
    result["weeks"] = weeks
    result["students"] = max(numStudents)
    result["hours"] = sum(hours)
    result["hours_average"] = result["hours"] // result["students"]
    result["exercises"] = sum(exercises)
    result["exercises_average"] = result["exercises"] // result["students"]

    return result


if __name__ == '__main__':
    allCourses = retrieve_all()
    print(allCourses)

    course = retrieve_course("docker2019")
    print(course)
