class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.minutes == 59 and self.seconds == 59:
            self.minutes = 0
            self.seconds = 0
            return

        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0

            if self.minutes < 60:
                self.minutes += 1
            else:
                self.minutes = 0

    def __str__(self):
        mins = str(self.minutes)
        secs = str(self.seconds)

        if self.minutes < 10:
            mins = f"0{self.minutes}"
        if self.seconds < 10:
            secs = f"0{self.seconds}"

        return f"{mins}:{secs}"


if __name__ == '__main__':
    watch = Stopwatch()
    for i in range(3611):
        print(watch)
        watch.tick()
