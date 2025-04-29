import logging
from dataclasses import dataclass, fields
from typing import Optional


@dataclass
class MortgageParameters:
    property_appraisal_usd: float = 0.00  # USD
    interest_yearly_percent: float = 0.00  # yearly, Percentage
    application_fee_one_time_usd: float = 0.00  # one-time, USD
    term_years: int = 0  # total years
    closing_cost_one_time_usd: float = 0.00  # one-time, USD
    down_payment_one_time_usd: float = 0.00  # one-time, USD


class Mortgage:
    def __init__(self, params: MortgageParameters, logger: Optional[logging.Logger] = None):
        for field in fields(params):
            setattr(self, field.name, getattr(params, field.name))

        self.logger: logging.Logger = logger if logger else logging.getLogger()

        self.paid_principal_usd = self.down_payment_one_time_usd
        self.initial_loan_usd = self.property_appraisal_usd - self.down_payment_one_time_usd

        if self.initial_loan_usd < 0:
            self.logger.error(
                "The paid principal completely covers the target property and there is no need for a mortgage."
            )
            self.initial_loan_usd = 0

        self.set_term()
        self.set_interest_rate()

    def set_interest_rate(self, interest_yearly_percent: Optional[float] = None) -> None:
        if interest_yearly_percent:
            self.interest_yearly_percent = interest_yearly_percent

        if self.interest_yearly_percent < 0:
            raise ValueError("Yearly interest rate must be non-negative.")

        self.interest_monthly = self.interest_yearly_percent / 12 / 100

    def set_term(self, term_years: Optional[int] = None) -> None:
        if term_years:
            self.term_years = term_years

        if self.term_years <= 0:
            raise ValueError("Loan term years must be greater than zero.")

        self.term_months = self.term_years * 12

    def update_paid_principal_usd(self, payment_usd: float) -> None:
        """
        Update the paid principal by adding `payment_usd`
        """
        if payment_usd < 0:
            raise ValueError("Payment amount must be non-negative.")
        self.paid_principal_usd += payment_usd

    def remaining_balance(self) -> float:
        """
        Returns the remaining loan balance after subtracting paid principal.
        """
        return max(self.initial_loan_usd - self.paid_principal_usd, 0)

    def monthly_payment(self) -> float:
        """
        Calculate the fixed total monthly mortgage payment based on the original loan amount and loan terms.
        """
        if self.paid_principal_usd >= self.initial_loan_usd:
            return 0.0

        if self.interest_monthly == 0:
            return self.initial_loan_usd / self.term_months

        projected_interest = (1 + self.interest_monthly) ** self.term_months
        monthly_payment = (
            self.initial_loan_usd
            * self.interest_monthly
            * projected_interest
            / (projected_interest - 1)
        )

        return monthly_payment

    def current_principal_payment(self) -> float:
        """
        Estimate the principal portion of the upcoming monthly mortgage payment,
        based on the current state of the mortgage.
        """
        total_monthly_payment = self.monthly_payment()
        current_balance = self.remaining_balance()
        monthly_interest = current_balance * self.interest_monthly
        return max(total_monthly_payment - monthly_interest, 0)
