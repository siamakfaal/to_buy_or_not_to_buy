from src.to_buy_or_not_to_buy.types.variables import Rental


def rental_initial_payment(rental_vars: Rental) -> float:
    """
    Calculate the total upfront payment for renting.
    """
    return rental_vars.application_fee_one_time_usd + rental_vars.car_down_payment_one_time_usd


def rental_monthly_payment(rental_vars: Rental) -> float:
    """
    Calculate the total monthly cost of renting.
    """
    monthly_prorated_cost = rental_vars.insurance_yearly_usd / 12

    recurring_monthly_cost = (
        rental_vars.rent_monthly_usd
        + rental_vars.utilities_monthly_usd
        + rental_vars.commute_cost_monthly_usd
        + rental_vars.gym_subscription_monthly_usd
        + rental_vars.car_payment_monthly_usd
    )

    return monthly_prorated_cost + recurring_monthly_cost
