# Note! Do not change the class Person!
class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        self.number_of_weigh_ins += 1
        return person.weight

    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.number_of_weigh_ins


if __name__ == '__main__':
    babyCenter = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"{eric.name} weighs {babyCenter.weigh(eric)} kg")
    print(f"{peter.name} weighs {babyCenter.weigh(peter)} kg")
    print()

    babyCenter.feed(eric)
    babyCenter.feed(eric)
    babyCenter.feed(eric)

    print(f"{eric.name} weighs {babyCenter.weigh(eric)} kg")
    print(f"{peter.name} weighs {babyCenter.weigh(peter)} kg")

    babyCenter2 = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"Total number of weigh-ins is {babyCenter2.weigh_ins()}")

    babyCenter2.weigh(eric)
    babyCenter2.weigh(eric)

    print(f"Total number of weigh-ins is {babyCenter2.weigh_ins()}")

    babyCenter2.weigh(eric)
    babyCenter2.weigh(eric)
    babyCenter2.weigh(eric)
    babyCenter2.weigh(eric)

    print(f"Total number of weigh-ins is {babyCenter2.weigh_ins()}")
