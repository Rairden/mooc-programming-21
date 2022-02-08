from datetime import datetime
from datetime import timedelta

filename = input("Filename: ")
startDate = input("Starting date: ")
numDays = int(input("How many days: "))

startDate = datetime.strptime(startDate, "%d.%m.%Y")
endDate = startDate + timedelta(days=numDays - 1)

print("Please type in screen time in minutes on each day (TV computer mobile):")

totalTime = 0
dailyMinutes = []

for i in range(numDays):
    date = startDate + timedelta(days=i)
    screenTime = input(f"Screen time {date.date()}: ")
    mins = screenTime.split(" ")
    scrnTime = sum(list(map(int, mins)))
    totalTime += scrnTime
    fmtDate = datetime.strftime(date, "%d.%m.%Y")
    dailyMinutes.append(f"{fmtDate}: {mins[0]}/{mins[1]}/{mins[2]}\n")

avgMins = totalTime / numDays

with open(filename, "w") as f:
    start = datetime.strftime(startDate, "%d.%m.%Y")
    end = datetime.strftime(endDate, "%d.%m.%Y")
    timePeriod = f"{start}-{end}"
    f.write(f"Time period: {timePeriod}\n")
    f.write(f"Total minutes: {totalTime}\n")
    f.write(f"Average minutes: {avgMins}\n")

    for d in dailyMinutes:
        f.write(d)

print(f"Data stored in file {filename}")
