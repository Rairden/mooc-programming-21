import json


def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()

    persons = json.loads(data)

    for p in persons:
        print(f"{p['name']} {p['age']} years", end="")
        hobbies = p["hobbies"]
        hobbs = " ("
        hobbs += str(hobbies).replace("[", "").replace("]", "").replace("'", "")
        # hobbies = ", ".join(p["hobbies"])   # proper technique
        hobbs += ")"
        print(hobbs)


if __name__ == '__main__':
    print_persons("file1.json")
