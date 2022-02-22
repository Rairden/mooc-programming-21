class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight


class Suitcase:
    def __init__(self, maxWeight):
        self.maxWeight = maxWeight
        self.suitcase = []

    def __str__(self):
        sumWeight = 0
        for item in self.suitcase:
            sumWeight += item.weight()

        string = f"{len(self.suitcase)} items ({sumWeight} kg)"

        if len(self.suitcase) == 1:
            string = string.replace("items", "item")

        return string

    def get_total_weight(self):
        totalWeight = 0
        for item in self.suitcase:
            totalWeight += item.weight()
        return totalWeight

    def add_item(self, thing: Item):
        totalWeight = self.get_total_weight()
        if totalWeight + thing.weight() <= self.maxWeight:
            self.suitcase.append(thing)

    def print_items(self):
        for item in self.suitcase:
            print(f"{item.name()} ({item.weight()} kg)")

    def weight(self):
        return self.get_total_weight()

    def heaviest_item(self):
        if len(self.suitcase) == 0:
            return None

        heaviest = 0
        result = None
        for item in self.suitcase:
            if item.weight() > heaviest:
                heaviest = item.weight()
                result = item

        return result


class CargoHold:
    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity

    def __str__(self):
        totalWeight = 0
        for suitCase in self.cargo:
            totalWeight += suitCase.get_total_weight()

        string = f"{len(self.cargo)} suitcases, space for {self.capacity - totalWeight} kg"

        if len(self.cargo) == 1:
            string = string.replace("suitcases", "suitcase")

        return string

    def add_suitcase(self, sc: Suitcase):
        if sc.get_total_weight() + sc.weight() <= self.capacity:
            self.cargo.append(sc)

    def print_items(self):
        for sc in self.cargo:
            for item in sc.suitcase:
                print(item)


def test1():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)
    print("------------------------------")


def test2():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)
    print("------------------------------")


def test4():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combinedWeight = suitcase.weight()
    print(f"Combined weight: {combinedWeight} kg")
    print("------------------------------")


def test5():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")
    print("------------------------------")


def test6():
    cargoHold = CargoHold(1000)
    print(cargoHold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    eriksSuitcase = Suitcase(10)
    eriksSuitcase.add_item(book)
    eriksSuitcase.add_item(phone)

    ryansSuitcase = Suitcase(10)
    ryansSuitcase.add_item(brick)

    cargoHold.add_suitcase(eriksSuitcase)
    print(cargoHold)

    cargoHold.add_suitcase(ryansSuitcase)
    print(cargoHold)
    print("------------------------------")


def test7():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    eriksSuitcase = Suitcase(10)
    eriksSuitcase.add_item(book)
    eriksSuitcase.add_item(phone)

    ryansSuitcase = Suitcase(10)
    ryansSuitcase.add_item(brick)

    cargoHold = CargoHold(1000)
    cargoHold.add_suitcase(eriksSuitcase)
    cargoHold.add_suitcase(ryansSuitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargoHold.print_items()


if __name__ == '__main__':
    test1()
    test2()
    test4()
    test5()
    test6()
    test7()
