from src.to_buy_or_not_to_buy.types.variables import Rental


def rental_initial_payment(rental_vars: Rental) -> float:
    """
    Calculate the total upfront payment for renting.
    """
    return rental_vars.application_fee + rental_vars.car_down_payment


def rental_monthly_payment(rental_vars: Rental) -> float:
    """
    Calculate the total monthly cost of renting.
    """
    total_monthly_cost = (
        rental_vars.insurance / 12
        + rental_vars.rent
        + rental_vars.utilities
        + rental_vars.commute_cost
        + rental_vars.gym_subscription
        + rental_vars.car_payment
    )
    return total_monthly_cost
