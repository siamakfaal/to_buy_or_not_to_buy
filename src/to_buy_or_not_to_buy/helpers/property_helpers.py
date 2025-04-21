from src.to_buy_or_not_to_buy.helpers.mortgage_helpers import mortgage_monthly_payment
from src.to_buy_or_not_to_buy.types.variables import Mortgage, OwnedProperty


def property_initial_payment(property: OwnedProperty, mortgage: Mortgage) -> float:
    """
    Calculate the total upfront payment for purchasing the property,
    including repairs, car down payment, and mortgage-related fees.
    """
    upfront_cost = (
        property.repair
        + property.car_down_payment
        + mortgage.application_fee
        + mortgage.closing_cost
        + mortgage.down_payment
    )
    return upfront_cost


def property_monthly_payment(property: OwnedProperty, mortgage: Mortgage) -> float:
    """
    Calculate the total monthly cost of owning the property,
    including prorated yearly costs and recurring expenses.
    """
    yearly_cost = property.insurance + property.maintenance + property.tax

    total_monthly_cost = (
        yearly_cost / 12
        + property.utilities
        + property.commute_cost
        + property.gym_subscription
        + property.car_payment
        + property.hoa
        + mortgage_monthly_payment(mortgage)
    )
    return total_monthly_cost
