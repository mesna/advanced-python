import csv
from collections import namedtuple
from datetime import datetime

from .number_utils import NumberUtils
from .info_bit import InfoBit

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

        greatest_increase_over_prev_day = self.greatest_increase_over_prev_day(price_data)

    def greatest_increase_over_prev_day(self, price_data):
        biggest_change = 0
        date_of_biggest_change = None
        increase_percentage = 0

        for i in range(len(price_data) - 1):
            previous = price_data[i].price
            current = price_data[i + 1].price
            change = current - previous
            if change > biggest_change:
                biggest_change = change
                date_of_biggest_change = price_data[i + 1].date
                increase_percentage = NumberUtils.calculate_percentage_increase(previous, current)

        return InfoBit(description="Greatest percent increase over the previous day",
                       value=increase_percentage,
                       date=date_of_biggest_change)
