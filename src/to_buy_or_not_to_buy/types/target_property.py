import logging
from dataclasses import dataclass, fields
from typing import Optional

from .mortgage import Mortgage


@dataclass
class TargetPropertyParameters:
    final_purchase_price_usd: float = 0.00  # USD
    covered_appraisal_gap: float = 0.00  # onetime, USD
    tax_yearly_usd: float = 0.00  # yearly, USD
    maintenance_monthly_usd: float = 0.00  # monthly, USD
    initial_repair_one_time_usd: float = 0.00  # one-time, USD
    remodeling_one_time_usd: float = 0.00  # one-time, USD
    utilities_monthly_usd: float = 0.00  # monthly, USD
    insurance_yearly_usd: float = 0.00  # yearly, USD
    hoa_monthly_usd: float = 0.00  # monthly, USD
    appreciation_yearly_percent: float = 0.00  # yearly, Percentage
    commute_cost_monthly_usd: float = 0.00  # monthly, USD
    gym_subscription_monthly_usd: float = 0.00  # monthly, USD
    car_payment_monthly_usd: float = 0.00  # monthly, USD
    car_down_payment_one_time_usd: float = 0.00  # one-time, USD


class TargetProperty:
    def __init__(self, params: TargetPropertyParameters, logger: Optional[logging.Logger] = None):
        for field in fields(params):
            setattr(self, field.name, getattr(params, field.name))

        self.logger: logging.Logger = logger if logger else logging.getLogger()
        self.set_appreciation_monthly()

    def set_appreciation_monthly(self, appreciation_yearly_percent: Optional[float] = None) -> None:
        if appreciation_yearly_percent:
            self.appreciation_yearly_percent = appreciation_yearly_percent
        self.appreciation_monthly = self.appreciation_yearly_percent / 12 / 100

    def initial_payment(self, mortgage: Mortgage) -> float:
        """
        Calculate the total upfront payment for purchasing the property,
        including repairs, car down payment, and mortgage-related fees.
        """
        upfront_cost = (
            self.initial_repair_one_time_usd
            + self.car_down_payment_one_time_usd
            + mortgage.application_fee_one_time_usd
            + mortgage.closing_cost_one_time_usd
            + mortgage.down_payment_one_time_usd
        )

        appraisal_gap_payment = min(
            max(self.final_purchase_price_usd - mortgage.property_appraisal_usd, 0),
            self.covered_appraisal_gap,
        )
        if appraisal_gap_payment > 0:
            self.logger.info(f"Covering appraisal gap of ${appraisal_gap_payment:.2f} USD.")

        return upfront_cost + appraisal_gap_payment

    def monthly_payment(self, mortgage: Mortgage) -> float:
        """
        Calculate the total monthly cost of owning the property,
        including prorated yearly costs and recurring expenses.
        """
        # Convert yearly costs to monthly
        monthly_prorated_cost = (self.insurance_yearly_usd + self.tax_yearly_usd) / 12

        recurring_monthly_cost = (
            self.maintenance_monthly_usd
            + self.utilities_monthly_usd
            + self.commute_cost_monthly_usd
            + self.gym_subscription_monthly_usd
            + self.car_payment_monthly_usd
            + self.hoa_monthly_usd
        )

        total_monthly_cost = (
            monthly_prorated_cost + recurring_monthly_cost + mortgage.monthly_payment()
        )
        return total_monthly_cost

    def current_value(self, months_from_purchase: int) -> float:
        """
        Calculate property value based on the yearly appreciation
        """
        return self.final_purchase_price_usd * (
            1 + self.appreciation_monthly * months_from_purchase
        )
