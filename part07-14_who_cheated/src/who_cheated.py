from datetime import datetime
from datetime import timedelta


def cheaters():
    """That is, any student whose any task was handed in over 3 hours later than their
    exam start time is labelled a cheater. There may be more than one submission for the same task for each student."""
    startTimes = {}
    submissions = {}
    cheaters = []
    with open("start_times.csv", "r") as start_csv, open("submissions.csv", "r") as subm_csv:
        for line in start_csv:
            ln = line.strip().split(";")
            student = ln[0]

            time = ln[1].split(":")
            hr = int(time[0])
            mins = int(time[1])
            start = datetime(1, 1, 1, hr, mins)

            if student in startTimes and start < startTimes[student]:
                startTimes[student] = start
                continue
            startTimes[student] = start

        for line in subm_csv:
            ln = line.strip().split(";")
            student = ln[0]

            time = ln[3].split(":")
            hr = int(time[0])
            mins = int(time[1])
            handInTime = datetime(1, 1, 1, hr, mins)

            if student in submissions:
                submissions[student].append(handInTime)
                continue
            submissions[student] = [handInTime]

        for student in startTimes:
            subs = submissions[student]
            for sub in subs:
                upperLimit = startTimes[student] + timedelta(hours=3)
                if sub > upperLimit:
                    cheaters.append(student)
                    break

        return cheaters


if __name__ == '__main__':
    cheats = cheaters()
    print(cheats)
