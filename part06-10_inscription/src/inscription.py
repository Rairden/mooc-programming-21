name = input("Whom should I sign this to: ")
fileWrite = input("Where shall I save it: ")
text = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team\n"

with open(fileWrite, "w") as file:
    file.write(text)
