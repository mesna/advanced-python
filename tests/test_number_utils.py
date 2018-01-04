from unittest import TestCase
from advanced_python.number_utils import NumberUtils


class TestIfCorrectPercentageIncrease(TestCase):
    def test(self):
        start = 10.0
        end = 12.0

        correct_percentage = 20.0
        percentage = NumberUtils.calculate_percentage_increase(start, end)

        self.assertTrue(percentage == correct_percentage,
                        msg="Correct percentage increase is '{}', but got '{}'".format(correct_percentage, percentage))


class TestIfCorrectPercentageDecrease(TestCase):
    def test(self):
        start = 10.0
        end = 5.0

        correct_percentage = -50.0
        percentage = NumberUtils.calculate_percentage_increase(start, end)

        self.assertTrue(percentage == correct_percentage,
                        msg="Correct percentage decrease is '{}', but got '{}'".format(correct_percentage, percentage))