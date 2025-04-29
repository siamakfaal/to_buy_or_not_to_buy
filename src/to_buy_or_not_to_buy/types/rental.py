import logging
from dataclasses import dataclass, fields
from typing import Optional


@dataclass
class RentalParameters:
    application_fee_one_time_usd: float = 0.00  # one-time, USD
    rent_monthly_usd: float = 0.00  # monthly, USD
    utilities_monthly_usd: float = 0.00  # monthly, USD
    renter_insurance_yearly_usd: float = 0.00  # yearly, USD
    commute_cost_monthly_usd: float = 0.00  # monthly, USD
    gym_subscription_monthly_usd: float = 0.00  # monthly, USD
    car_payment_monthly_usd: float = 0.00  # monthly, USD
    car_down_payment_one_time_usd: float = 0.00  # one-time, USD


class Rental:
    def __init__(self, params: RentalParameters, logger: Optional[logging.Logger] = None):
        for field in fields(params):
            setattr(self, field.name, getattr(params, field.name))

        self.monthly_prorated_insurance_usd = self.renter_insurance_yearly_usd / 12
        self.logger: logging.Logger = logger if logger else logging.getLogger()

    def initial_payment_usd(self) -> float:
        """
        Calculate the total upfront payment for renting.
        """
        return self.application_fee_one_time_usd + self.car_down_payment_one_time_usd

    def monthly_payment_usd(self) -> float:
        """
        Calculate the total monthly cost of renting.
        """
        recurring_monthly_cost = (
            self.rent_monthly_usd
            + self.utilities_monthly_usd
            + self.commute_cost_monthly_usd
            + self.gym_subscription_monthly_usd
            + self.car_payment_monthly_usd
        )

        return self.monthly_prorated_insurance_usd + recurring_monthly_cost
