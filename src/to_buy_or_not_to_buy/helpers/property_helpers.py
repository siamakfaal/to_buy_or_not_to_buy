from src.to_buy_or_not_to_buy.helpers.mortgage_helpers import mortgage_monthly_payment
from src.to_buy_or_not_to_buy.types.variables import Mortgage, OwnedProperty


def property_initial_payment(property: OwnedProperty, mortgage: Mortgage) -> float:
    """
    Calculate the total upfront payment for purchasing the property,
    including repairs, car down payment, and mortgage-related fees.
    """
    upfront_cost = (
        property.initial_repair_one_time_usd
        + property.car_down_payment_one_time_usd
        + mortgage.application_fee_one_time_usd
        + mortgage.closing_cost_one_time_usd
        + mortgage.down_payment_one_time_usd
    )
    return upfront_cost


def property_monthly_payment(property: OwnedProperty, mortgage: Mortgage) -> float:
    """
    Calculate the total monthly cost of owning the property,
    including prorated yearly costs and recurring expenses.
    """
    # Convert yearly costs to monthly
    monthly_prorated_cost = (property.insurance_yearly_usd + property.tax_yearly_usd) / 12

    recurring_monthly_cost = (
        property.maintenance_monthly_usd
        + property.utilities_monthly_usd
        + property.commute_cost_monthly_usd
        + property.gym_subscription_monthly_usd
        + property.car_payment_monthly_usd
        + property.hoa_monthly_usd
    )

    total_monthly_cost = (
        monthly_prorated_cost + recurring_monthly_cost + mortgage_monthly_payment(mortgage)
    )
    return total_monthly_cost
