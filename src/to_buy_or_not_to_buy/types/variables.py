from dataclasses import dataclass


@dataclass
class Rental:
    application_fee_one_time_usd: float = 0.00  # one-time, USD
    rent_monthly_usd: float = 0.00  # monthly, USD
    utilities_monthly_usd: float = 0.00  # monthly, USD
    insurance_yearly_usd: float = 0.00  # yearly, USD
    commute_cost_monthly_usd: float = 0.00  # monthly, USD
    gym_subscription_monthly_usd: float = 0.00  # monthly, USD
    car_payment_monthly_usd: float = 0.00  # monthly, USD
    car_down_payment_one_time_usd: float = 0.00  # one-time, USD


@dataclass
class OwnedProperty:
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


@dataclass
class Mortgage:
    initial_loan_usd: float = 0.00  # one-time, USD
    paid_principal_usd: float = 0.00  # ongoing total, USD
    interest_yearly_percent: float = 0.00  # yearly, Percentage
    application_fee_one_time_usd: float = 0.00  # one-time, USD
    term_years: int = 0  # total years
    closing_cost_one_time_usd: float = 0.00  # one-time, USD
    down_payment_one_time_usd: float = 0.00  # one-time, USD


@dataclass
class Investment:
    balance_usd: float = 0.00  # current, USD
    interest_yearly_percent: float = 0.00  # yearly, Percentage
    budget_monthly_usd: float = 0.00  # monthly, USD
    tax_yearly_percent: float = 0.00  # yearly, Percentage


@dataclass
class Variables:
    # --- Rental Costs ---
    rental: Rental

    # --- Property Ownership Costs ---
    owned_property: OwnedProperty

    # --- Mortgage Costs ---
    mortgage: Mortgage

    # --- Investment ---
    investment: Investment
