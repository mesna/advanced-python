class InfoBit:
    def __init__(self, description, value, date):
        self.__description = description
        self.__value = value
        self.__date = date

    def description(self):
        return self.__description

    def value(self):
        return self.__value

    def date(self):
        return self.__date

    def __str__(self):
        return "[description={}, value={}, date={}]".format(self.description(), self.__value, self.__date)