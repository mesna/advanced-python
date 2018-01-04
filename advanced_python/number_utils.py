class NumberUtils:
    def __init__(self):
        pass

    @staticmethod
    def calculate_percentage_increase(start_value, end_value):
        change = end_value - start_value
        percentage_increase = change * 100.0 / start_value
        return percentage_increase
