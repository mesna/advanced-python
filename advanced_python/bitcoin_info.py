class BitcoinInfo:
    def __init__(self,
                 greatest_percent_increase_over_prev_day,
                 greatest_percent_decrease_over_prev_day,
                 highest_price):

        self.__greatest_percent_increase_over_prev_day = greatest_percent_increase_over_prev_day
        self.__greatest_percent_decrease_over_prev_day = greatest_percent_decrease_over_prev_day
        self.__highest_price = highest_price

    def greatest_percent_increase_over_prev_day(self):
        return self.__greatest_percent_increase_over_prev_day

    def greatest_percent_decrease_over_prev_day(self):
        return self.__greatest_percent_decrease_over_prev_day

    def highest_price(self):
        return self.__highest_price
