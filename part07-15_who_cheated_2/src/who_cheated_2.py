from datetime import datetime
from datetime import timedelta


def final_points():
    """Returns the total task points for each student.
    If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
    If the submission was made over 3 hours after the start time, the submission is ignored."""
    startTimes = {}
    submissions = {}
    with open("start_times.csv", "r") as start_csv, open("submissions.csv", "r") as subm_csv:
        for line in start_csv:
            ln = line.strip().split(";")
            student = ln[0]
            time = ln[1]
            start = datetime.strptime(time, "%H:%M")

            if student in startTimes and start < startTimes[student]:
                startTimes[student] = start
                continue
            startTimes[student] = start

        for line in subm_csv:
            ln = line.strip().split(";")
            student = ln[0]
            task = ln[1]
            pts = int(ln[2])
            time = ln[3]
            time = datetime.strptime(time, "%H:%M")

            if student not in submissions:
                tasks = {}
                submissions[student] = tasks
                tasks[task] = pts
                continue

            upperLimit = startTimes[student] + timedelta(hours=3)
            if time > upperLimit:
                continue

            if task in submissions[student]:
                if submissions[student][task] < pts:
                    submissions[student][task] = pts
            else:
                submissions[student][task] = pts

        for student, pts in submissions.items():
            totalPts = sum(pts.values())
            submissions[student] = totalPts

        return submissions


if __name__ == '__main__':
    finalPts = final_points()
    print(finalPts)
