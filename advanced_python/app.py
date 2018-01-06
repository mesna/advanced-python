from .csv_parser import CsvParser


class App:
    def __init__(self, csv_parser):
        if not isinstance(csv_parser, CsvParser):
            raise ValueError("I did not get CSV parser object.")

        self.__csv_parser = csv_parser

    def print_info(self):
        bitcoin_info = self.__csv_parser.parse()
