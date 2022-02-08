from datetime import datetime


day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

newYearsEve = datetime(1999, 12, 31)
date = datetime(year, month, day)

diff = newYearsEve - date

if diff.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {diff.days} days old on the eve of the new millennium.")
