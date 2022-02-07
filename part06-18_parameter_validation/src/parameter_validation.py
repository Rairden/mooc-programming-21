def new_person(name: str, age: int):
    if name == "":
        raise ValueError("The string was empty")
    if " " not in name:
        raise ValueError("Name must be at least two words")
    if len(name) > 40:
        raise ValueError("Name must not exceed 40 characters")
    if not 0 <= age <= 150:
        raise ValueError("Age must be greater than 0 and less than 150")

    return name, age


if __name__ == '__main__':
    person = new_person("Casey Muratori", 14)
