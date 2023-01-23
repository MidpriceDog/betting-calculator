import unittest
import numpy as np
import odds_converter as oc
from fractions import Fraction
from decimal import Decimal


class TestOddsConverter(unittest.TestCase):

    def setUp(self):
        # Parallel array of equivalent odds expressed in different ways
        self.decimal_odds = np.array([1.25, 2.0, 3.0, 5.0, 14.0])
        self.fractional_odds = np.array([Fraction(1, 4), Fraction(
            1, 1), Fraction(2, 1), Fraction(4, 1), Fraction(13, 1)])
        self.american_odds = np.array([-400, 100, 200, 400, 1300])
        self.n = len(self.american_odds)

    def odds_converter_helper(self, function, input_odds, result_odds):
        for i in range(self.n):
            converted_odds = function(input_odds[i])
            self.assertEqual(converted_odds, result_odds[i])

    def test_american_to_decimal(self):
        self.odds_converter_helper(
            oc.american_to_decimal, self.american_odds, self.decimal_odds)

    def test_american_to_fractional(self):
        self.odds_converter_helper(
            oc.american_to_fractional, self.american_odds, self.fractional_odds)

    def test_decimal_to_american(self):
        self.odds_converter_helper(
            oc.decimal_to_american, self.decimal_odds, self.american_odds)

    def test_decimal_to_fractional(self):
        self.odds_converter_helper(
            oc.decimal_to_fractional, self.decimal_odds, self.fractional_odds)

    def test_fractional_to_american(self):
        self.odds_converter_helper(
            oc.fractional_to_american, self.fractional_odds, self.american_odds)

    def test_fractional_to_decimal(self):
        self.odds_converter_helper(
            oc.fractional_to_decimal, self.fractional_odds, self.decimal_odds)


if __name__ == '__main__':
    unittest.main()
