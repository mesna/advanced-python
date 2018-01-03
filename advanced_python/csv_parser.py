import csv
from collections import namedtuple
from datetime import datetime

PricePoint = namedtuple('PricePoint', ['date', 'price'])


class CsvParser:
    def __init__(self, file_path):
        self.__file_path = file_path

    def parse(self):
        print "Parsing file '{}'.".format(self.__file_path)

        with open(self.__file_path, 'rb') as csv_file:
            raw_data = [tuple(line) for line in csv.reader(csv_file)]

        price_data = [PricePoint(date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S"),
                                 price=float(price)) for date, price in raw_data]
