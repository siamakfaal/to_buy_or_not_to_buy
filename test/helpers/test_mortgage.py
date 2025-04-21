import unittest

from src.to_buy_or_not_to_buy.helpers.mortgage_helpers import (
    current_principal_payment,
    mortgage_monthly_payment,
    remaining_balance,
)
from src.to_buy_or_not_to_buy.types.variables import Mortgage


class TestMortgageCalculations(unittest.TestCase):

    def setUp(self):
        # Default mortgage fixture
        self.default_mortgage_args = dict(
            initial_loan=100_000,
            interest=3.5,
            term=30,
            application_fee=300,
            closing_cost=2_000,
            down_payment=20_000,
            paid_principal=0.0,
        )

    def make_mortgage(self, **overrides):
        args = self.default_mortgage_args.copy()
        args.update(overrides)
        return Mortgage(**args)

    def test_monthly_payment_normal(self):
        mortgage = self.make_mortgage(initial_loan=300_000, interest=4.0, term=30)
        payment = mortgage_monthly_payment(mortgage)
        self.assertAlmostEqual(payment, 1432.25, places=2)

    def test_monthly_payment_zero_interest(self):
        mortgage = self.make_mortgage(initial_loan=120_000, interest=0.0, term=10)
        payment = mortgage_monthly_payment(mortgage)
        self.assertEqual(payment, 1000.0)

    def test_remaining_balance(self):
        mortgage = self.make_mortgage(paid_principal=20_000)
        balance = remaining_balance(mortgage)
        self.assertEqual(balance, 80_000)

    def test_remaining_balance_overpaid(self):
        mortgage = self.make_mortgage(paid_principal=150_000)
        balance = remaining_balance(mortgage)
        self.assertEqual(balance, 0)

    def test_current_principal_payment(self):
        mortgage = self.make_mortgage(initial_loan=200_000, interest=5.0, paid_principal=50000)
        principal = current_principal_payment(mortgage)
        self.assertGreater(principal, 0)
        self.assertLess(principal, mortgage_monthly_payment(mortgage))

    def test_current_principal_payment_fully_paid(self):
        mortgage = self.make_mortgage(paid_principal=100000)
        print(mortgage)
        print(f"{remaining_balance(mortgage) = }")
        principal = current_principal_payment(mortgage)
        self.assertEqual(principal, 0.0)


if __name__ == "__main__":
    unittest.main()
