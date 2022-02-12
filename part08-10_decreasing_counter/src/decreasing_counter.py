class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.initVal = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initVal


if __name__ == '__main__':
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()
