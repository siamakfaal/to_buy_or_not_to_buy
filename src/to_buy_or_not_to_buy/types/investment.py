import logging
from dataclasses import dataclass
from typing import Optional


@dataclass
class InvestmentParameters:
    balance_usd: float = 0.00  # current, USD
    interest_yearly_percent: float = 0.00  # yearly, Percentage
    monthly_contribution_usd: float = 0.00  # monthly, USD
    tax_yearly_percent: float = 0.00  # yearly, Percentage


@dataclass
class InvestmentAddedValue:
    added_contribution_usd: float = 0.00
    interest_earned_usd: float = 0.00
    tax_liability_usd: float = 0.00


class Investment:
    def __init__(self, params: InvestmentParameters, logger: Optional[logging.Logger] = None):
        self.balance_usd: float = params.balance_usd
        self.monthly_contribution_usd: float = params.monthly_contribution_usd
        self.interest_yearly_percent: float = params.interest_yearly_percent
        self.tax_yearly_percent: float = params.tax_yearly_percent

        self.logger: logging.Logger = logger if logger else logging.getLogger()

    def update_balance(self, amount_usd: float) -> None:
        self.balance_usd += amount_usd

    def set_monthly_contribution_usd(self, amount_usd: float) -> None:
        if amount_usd < 0:
            raise ValueError("Monthly contribution cannot be negative.")
        self.monthly_contribution_usd = amount_usd

    def calculate_monthly_added_value(self) -> InvestmentAddedValue:
        """Calculates the monthly contribution, interest earned, and tax liability
        based on the current state of the investment. This function does not
        modify the investment's current state.
        """
        total_balance = self.balance_usd + self.monthly_contribution_usd
        interest_earning = total_balance * (self.interest_yearly_percent / 100) / 12
        return InvestmentAddedValue(
            added_contribution_usd=self.monthly_contribution_usd,
            interest_earned_usd=interest_earning,
            tax_liability_usd=interest_earning * self.tax_yearly_percent / 100,
        )

    def apply_monthly_return(
        self, added_value: Optional[InvestmentAddedValue] = None, apply_tax: bool = True
    ):
        """
        Updates the investment balance by adding the contribution and interest.
        If `apply_tax` is True, subtracts the calculated tax liability from the net value.
        """
        if not added_value:
            self.logger.debug(
                f"No InvestmentAddedValue provided. Recalculating monthly return using current balance {self.balance_usd:.2f} and monthly contribution {self.monthly_contribution_usd:.2f}"
            )
            added_value = self.calculate_monthly_added_value()

        net_value = added_value.added_contribution_usd + added_value.interest_earned_usd

        if apply_tax:
            net_value -= added_value.tax_liability_usd

        self.balance_usd += net_value
