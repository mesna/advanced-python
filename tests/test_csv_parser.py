from unittest import TestCase

from datetime import datetime

from advanced_python import CsvParser, NumberUtils
from advanced_python import PricePoint

raw_data = [('2017-01-02 00:00:00', 10),
            ('2017-01-03 00:00:00', 8),
            ('2017-01-04 00:00:00', 5),
            ('2017-01-05 00:00:00', 9),
            ('2017-01-06 00:00:00', 11)]

GREATEST_INCREASE_INDEX = 3
GREATEST_DECREASE_INDEX = 2
HIGHEST_PRICE_IN_DATA_INDEX = 4

price_data = [PricePoint(date=datetime.strptime(date, "%Y-%m-%d %H:%M:%S"),
                         price=float(price)) for date, price in raw_data]


class TestGreatestIncreaseOverPreviousDay(TestCase):
    def test(self):
        csv_parser = CsvParser("")

        greatest_increase_over_previous_day = csv_parser.greatest_increase_over_prev_day(price_data)

        date = greatest_increase_over_previous_day.date()
        percentage = greatest_increase_over_previous_day.value()

        correct_date = price_data[GREATEST_INCREASE_INDEX].date
        correct_percentage = NumberUtils.calculate_percentage_increase(price_data[GREATEST_INCREASE_INDEX - 1].price,
                                                                       price_data[GREATEST_INCREASE_INDEX].price)

        self.assertTrue(date == correct_date,
                        msg="Correct date should be '{}', but it is '{}'".format(correct_date, date))

        self.assertTrue(percentage == correct_percentage,
                        msg="Correct percentage should be '{}', but it is '{}'".format(percentage, correct_percentage))


class TestGreatestDecreaseOverPreviousDay(TestCase):
    def test(self):
        csv_parser = CsvParser("")

        greatest_decrease_over_previous_day = csv_parser.greatest_decrease_over_prev_day(price_data)

        date = greatest_decrease_over_previous_day.date()
        percentage = greatest_decrease_over_previous_day.value()

        correct_date = price_data[GREATEST_DECREASE_INDEX].date
        correct_percentage = NumberUtils.calculate_percentage_increase(price_data[GREATEST_DECREASE_INDEX - 1].price,
                                                                       price_data[GREATEST_DECREASE_INDEX].price)

        self.assertTrue(date == correct_date,
                        msg="Correct date should be '{}', but it is '{}'".format(correct_date, date))

        self.assertTrue(percentage == correct_percentage,
                        msg="Correct percentage should be '{}', but it is '{}'".format(percentage, correct_percentage))



class TestHighestPriceInData(TestCase):
    def test(self):
        csv_parser = CsvParser("")

        highest_price_in_data = csv_parser.highest_price_in_data(price_data)

        date = highest_price_in_data.date()
        price = highest_price_in_data.value()

        correct_date = price_data[HIGHEST_PRICE_IN_DATA_INDEX].date
        correct_price = price_data[HIGHEST_PRICE_IN_DATA_INDEX].price

        self.assertTrue(date == correct_date,
                        msg="Correct date should be '{}', but it is '{}'".format(correct_date, date))

        self.assertTrue(price == correct_price,
                        msg="Correct price should be '{}', but it is '{}'".format(price, correct_price))

