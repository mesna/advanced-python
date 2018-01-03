class InfoBit:
    def __init__(self, description, value, day):
        self.__description = description
        self.__value = value
        self.__day = day

    def description(self):
        return self.__description

    def value(self):
        return self.__value

    def day(self):
        return self.__day
