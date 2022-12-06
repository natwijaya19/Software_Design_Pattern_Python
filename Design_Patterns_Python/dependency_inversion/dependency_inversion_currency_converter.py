from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List


class CurrencyConverterInterface(ABC):
    @abstractmethod
    def convert(self, amount: Decimal, from_currency: str, to_currency: str) -> Decimal:
        pass


class FXConverter(CurrencyConverterInterface):
    def __init__(self, fx_rates: List[FXRate]) -> None:
        self.fx_rates = fx_rates

    def convert(self, amount: Decimal, from_currency: str, to_currency: str) -> Decimal:
        if from_currency == to_currency:
            return amount

        from_rate = self._get_rate(from_currency)
        to_rate = self._get_rate(to_currency)

        return amount * (to_rate / from_rate)

    def _get_rate(self, currency: str) -> Decimal:
        for rate in self.fx_rates:
            if rate.currency == currency:
                return rate.rate

        raise Exception(f"Rate for {currency} not found")


class AlphaRate:
    def __init__(self, currency: str, rate: Decimal) -> None:
        self.currency = currency
        self.rate = rate

class FXRate:
    def __init__(self, currency: str, rate: Decimal) -> None:
        self.currency = currency
        self.rate = rate



class AplhaCurrency(CurrencyConverterInterface):
    def __init__(self, alpha_rates: List[AlphaRate]) -> None:
        self.alpha_rates = alpha_rates

    def convert(self, amount: Decimal, from_currency: str, to_currency: str) -> Decimal:
        if from_currency == to_currency:
            return amount

        from_rate = self._get_rate(from_currency)
        to_rate = self._get_rate(to_currency)

        return amount * (to_rate / from_rate)

    def _get_rate(self, currency: str) -> Decimal:
        for rate in self.alpha_rates:
            if rate.currency == currency:
                return rate.rate

        raise Exception(f"Rate for {currency} not found")


class App:
    def __init__(self, converter: CurrencyConverterInterface):
        self.converter = converter

    def start(self):
        amount = Decimal(100)
        print(f"Converting {amount} USD to EUR")
        print(f"Result: {self.converter.convert(amount, 'USD', 'EUR')} EUR")


if __name__ == "__main__":
    fx_rates = [
        FXRate('USD', Decimal(1)),
        FXRate('EUR', Decimal(0.9)),
        FXRate('GBP', Decimal(0.8)),
    ]
    alpha_rates = [
        AlphaRate('USD', Decimal(1)),
        AlphaRate('EUR', Decimal(0.9)),
        AlphaRate('GBP', Decimal(0.8)),
    ]
    fx_converter = FXConverter(fx_rates)
    alpha_converter = AplhaCurrency(alpha_rates)
    app = App(fx_converter)
    app.start()
    app = App(alpha_converter)
    app.start()
