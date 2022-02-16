class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError("length should be greater than 0")
        self.__length = length

    # A getter method
    @property
    def length(self):
        return self.__length

    # A setter method
    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError("length should be greater than 0")
        self.__length = length


if __name__ == '__main__':
    theWall = Recording(43)
    print(theWall.length)
    theWall.length = 44
    print(theWall.length)
