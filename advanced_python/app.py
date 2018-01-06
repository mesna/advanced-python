from .csv_parser import CsvParser


class App:
    def __init__(self, csv_parser):
        if not isinstance(csv_parser, CsvParser):
            raise ValueError("I did not get CSV parser object.")

        self.__csv_parser = csv_parser

    def print_info(self):
        bitcoin_info = self.__csv_parser.parse()

        greatest_increase_prev_day = bitcoin_info.greatest_percent_increase_over_prev_day()
        greatest_decrease_prev_day = bitcoin_info.greatest_percent_decrease_over_prev_day()
        highest_price = bitcoin_info.highest_price()

        greatest_increase_prev_day_info = "{} was {} in {}".format(greatest_increase_prev_day.description(),
                                                                   greatest_increase_prev_day.value(),
                                                                   self.format_date(greatest_increase_prev_day.date()))

        greatest_decrease_prev_day_info = "{} was {} in {}".format(greatest_decrease_prev_day.description(),
                                                                   greatest_decrease_prev_day.value(),
                                                                   self.format_date(greatest_decrease_prev_day.date()))

        highest_price_info = "{} was {} in {}".format(highest_price.description(),
                                                      highest_price.value(),
                                                      self.format_date(highest_price.date()))

        print "****************************************************************************************************"
        print "************************************ Bitcoin price information *************************************"
        print "****************************************************************************************************"
        print ""
        print greatest_increase_prev_day_info
        print greatest_decrease_prev_day_info
        print highest_price_info
        print ""
        print "****************************************************************************************************"

    def format_date(self, datetime):
        return "{}th of {} in year {}".format(datetime.day, datetime.strftime("%b"), datetime.year)
