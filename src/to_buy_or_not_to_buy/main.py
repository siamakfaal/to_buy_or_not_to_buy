import logging

from src.to_buy_or_not_to_buy.helpers.logger import create_logger
from src.to_buy_or_not_to_buy.helpers.plots import plot_wealth_over_iterations
from src.to_buy_or_not_to_buy.helpers.projected_wealth import property_purchase_gain
from src.to_buy_or_not_to_buy.types.investment import Investment, InvestmentParameters
from src.to_buy_or_not_to_buy.types.mortgage import Mortgage, MortgageParameters
from src.to_buy_or_not_to_buy.types.rental import Rental, RentalParameters
from src.to_buy_or_not_to_buy.types.target_property import TargetProperty, TargetPropertyParameters
from src.to_buy_or_not_to_buy.types.variables import InvestmentProfile


def main():
    logger = create_logger(name="projected_wealth", level=logging.DEBUG)

    rental_condition = RentalParameters(
        rent_monthly_usd=4_000.00,
        renter_insurance_yearly_usd=150.00,
    )

    investment_initial_condition = InvestmentParameters(
        balance_usd=140_000.00,
        interest_yearly_percent=4.00,
        monthly_contribution_usd=2_000.00,
        tax_yearly_percent=23.00,
    )

    target_property_info = TargetPropertyParameters(
        final_purchase_price_usd=800_000.00,
        covered_appraisal_gap=10_000.00,
        tax_yearly_usd=10_000.00,
        maintenance_monthly_usd=100.00,
        initial_repair_one_time_usd=40_000.00,
        remodeling_one_time_usd=40_000.00,
        utilities_monthly_usd=300.00,
        insurance_yearly_usd=2_000.00,
        appreciation_yearly_percent=5.00,
        commute_cost_monthly_usd=400.00,
        gym_subscription_monthly_usd=200.00,
        car_down_payment_one_time_usd=2_000,
        car_payment_monthly_usd=400.00,
    )

    mortgage_info = MortgageParameters(
        property_appraisal_usd=target_property_info.final_purchase_price_usd,
        application_fee_one_time_usd=300.00,
        term_years=30,
        closing_cost_one_time_usd=10_000.00,
        down_payment_one_time_usd=100_000.00,
    )

    profile = InvestmentProfile(
        rental=Rental(rental_condition, logger),
        investment=Investment(investment_initial_condition, logger),
        target_property=TargetProperty(target_property_info, logger),
        mortgage=Mortgage(mortgage_info, logger),
        investable_monthly_budget_usd=8_000.00,
    )

    # (TODO) Rent penalty for early termination

    iteration_details = property_purchase_gain(profile, 101, 96, logger)

    logger.info(f"Final update: {iteration_details[-1]}")

    plot_wealth_over_iterations(iteration_details)


if __name__ == "__main__":
    main()
