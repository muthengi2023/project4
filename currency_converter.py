#######################################################
# Currency Converter
#
# A simple project for currency conversion
#
# Name: Maureen Muthengi
# Section: 04
#
# Fall 2023
#########################################################
class Converter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency")

        rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount

    def update_rates(self, new_rates):
        self.exchange_rates.update(new_rates)

    def get_historical_rate(self, year, from_currency, to_currency):
        # Example: Assuming historical rates are stored in a nested dictionary
        historical_data = {
            2022: {'USD': 1.0, 'KES': 153, 'EUR': 0.92, 'GBP': 0.80, 'JPY': 147.89},
            2021: {'USD': 1.0, 'KES': 150, 'EUR': 0.95, 'GBP': 0.78, 'JPY': 145},
            # Add more years as needed
        }

        rates_for_year = historical_data.get(year, {})
        if rates_for_year:
            rate = rates_for_year.get(to_currency, None)
            if rate:
                return rate / rates_for_year.get(from_currency, None)
        return None


class CurrencyConverter(Converter):
    def __init__(self):
        # Exchange rates for common currencies
        exchange_rates = {'USD': 1.0, 'KES': 153, 'EUR': 0.92, 'GBP': 0.80, 'JPY': 147.89}
        # Add African currencies and their exchange rates with USD, including KES for Kenya
        african_currencies = {'KES': 153, 'NGN': 410, 'ZAR': 16.50, 'GHS': 11.50, 'EGP': 15.70}
        exchange_rates.update(african_currencies)
        super().__init__(exchange_rates)


if __name__ == "__main__":
    # Create an instance of CurrencyConverter
    currency_converter = CurrencyConverter()

    # Convert 100 USD to KES
    amount_to_convert = 100
    from_currency = 'USD'
    to_currency = 'KES'

    converted_amount = currency_converter.convert(amount_to_convert, from_currency, to_currency)

    print(f"{amount_to_convert} {from_currency} is equal to {converted_amount} {to_currency}")

    # Compare African currencies with USD
    african_currencies = ['KES', 'NGN', 'ZAR', 'GHS', 'EGP']
    print("Comparing African currencies with USD:")
    for african_currency in african_currencies:
        converted_amount_africa = currency_converter.convert(amount_to_convert, from_currency, african_currency)
        print(f"{amount_to_convert} {from_currency} is equal to {converted_amount_africa} {african_currency}")

    # Get historical rate
    historical_year = 2021
    historical_rate = currency_converter.get_historical_rate(historical_year, from_currency, to_currency)

    if historical_rate is not None:
        print(f"Historical rate in {historical_year}: {historical_rate}")
    else:
        print(f"No historical rate found for {historical_year}")
