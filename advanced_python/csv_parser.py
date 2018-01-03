class CsvParser:
    def __init__(self, file_path):
        self.__file_path = file_path

    def parse(self):
        print "Parsing file '{}'.".format(self.__file_path)
