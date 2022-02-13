class Clock:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def tick(self):
        if self.hr == 23 and self.min == 59 and self.sec == 59:
            self.hr = 0
            self.min = 0
            self.sec = 0
            return

        if self.min == 59 and self.sec == 59:
            self.min = 0
            self.sec = 0
            return

        if self.sec < 59:
            self.sec += 1
        else:
            self.sec = 0

            if self.min < 60:
                self.min += 1
            else:
                self.min = 0

    def set(self, hr, min):
        self.hr = hr
        self.min = min
        self.sec = 0

    def __str__(self):
        return f"{self.hr:02}:{self.min:02}:{self.sec:02}"


if __name__ == '__main__':
    clock = Clock(12, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
