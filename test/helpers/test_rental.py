import unittest

from src.to_buy_or_not_to_buy.helpers.rental_helpers import (
    rental_initial_payment,
    rental_monthly_payment,
)
from src.to_buy_or_not_to_buy.types.variables import Rental


class TestRentalPayments(unittest.TestCase):
    def setUp(self):
        self.rental = Rental(
            application_fee_one_time_usd=100.0,
            rent_monthly_usd=1200.0,
            utilities_monthly_usd=150.0,
            insurance_yearly_usd=600.0,
            commute_cost_monthly_usd=75.0,
            gym_subscription_monthly_usd=50.0,
            car_payment_monthly_usd=300.0,
            car_down_payment_one_time_usd=2000.0,
        )

    def test_rental_initial_payment(self):
        expected = 100.0 + 2000.0
        result = rental_initial_payment(self.rental)
        self.assertAlmostEqual(result, expected, places=2)

    def test_rental_monthly_payment(self):
        expected = (
            600.0 / 12  # insurance per month
            + 1200.0  # rent
            + 150.0  # utilities
            + 75.0  # commute
            + 50.0  # gym
            + 300.0  # car
        )
        result = rental_monthly_payment(self.rental)
        self.assertAlmostEqual(result, expected, places=2)


if __name__ == "__main__":
    unittest.main()
