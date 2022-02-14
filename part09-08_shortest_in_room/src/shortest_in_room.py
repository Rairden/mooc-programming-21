import operator


class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def print_contents(self):
        if self.is_empty():
            return

        combinedHeight = sum(p.height for p in self.persons)

        print(f"There are {len(self.persons)} persons in the room, "
              f"and their combined height is {combinedHeight} cm")

        for p in self.persons:
            print(f"{p.name} ({p.height})")

    def is_empty(self):
        return len(self.persons) == 0

    def shortest(self):
        if self.is_empty():
            return None

        self.persons.sort(key=operator.attrgetter("height"))
        return self.persons[0]

    def remove_shortest(self):
        if not self.is_empty():
            self.shortest()
            shortest = self.persons[0]
            del self.persons[0]
            return shortest


def test1():
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()
    print("########################################")


def test2():
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()
    print("########################################")


def test3():
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
    print("########################################")


if __name__ == '__main__':
    test1()
    test2()
    test3()
