####################################################
# Currency Converter
#
# Unit tests for currency converter
#
# Name: Maureen Muthengi
# Section: 04
#
# Fall 2023
#########################################################

import unittest
from currency_converter import CurrencyConverter  # Import the CurrencyConverter class

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        # Create an instance of CurrencyConverter for testing
        self.currency_converter = CurrencyConverter()

    def test_convert(self):
        # Test the convert method
        amount_to_convert = 100
        from_currency = 'USD'
        to_currency = 'KES'

        converted_amount = self.currency_converter.convert(amount_to_convert, from_currency, to_currency)

        # Assert that the converted amount is greater than 0
        self.assertGreater(converted_amount, 0)

    def test_historical_rate(self):
        # Test the get_historical_rate method
        historical_year = 2021
        from_currency = 'USD'
        to_currency = 'KES'

        historical_rate = self.currency_converter.get_historical_rate(historical_year, from_currency, to_currency)

        # Assert that the historical rate is not None
        self.assertIsNotNone(historical_rate)

    def test_invalid_currency(self):
        # Test for an invalid currency
        amount_to_convert = 100
        from_currency = 'USD'
        to_currency = 'INVALID'

        # Assert that attempting to convert with an invalid currency raises a ValueError
        with self.assertRaises(ValueError):
            self.currency_converter.convert(amount_to_convert, from_currency, to_currency)

if __name__ == '__main__':
    unittest.main()