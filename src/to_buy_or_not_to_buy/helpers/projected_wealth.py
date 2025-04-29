import logging
from typing import List

from src.to_buy_or_not_to_buy.types.variables import InvestmentProfile, IterationDetail


def property_purchase_gain(
    profile: InvestmentProfile, purchase_month: int, planning_horizon: int, logger: logging.Logger
) -> List[IterationDetail]:

    fixed_monthly_rent_payment_usd = profile.rental.monthly_payment_usd()
    fixed_monthly_property_payment_usd = profile.target_property.monthly_payment(profile.mortgage)

    if profile.investable_monthly_budget_usd < fixed_monthly_property_payment_usd:
        logger.error(
            f"Monthly investable budget {profile.investable_monthly_budget_usd:.2f} is less than monthly fixed mortgage payment of {fixed_monthly_property_payment_usd:.2f}"
        )
        return

    if profile.investable_monthly_budget_usd < fixed_monthly_rent_payment_usd:
        logger.error(
            f"Monthly investable budget {profile.investable_monthly_budget_usd:.2f} is less than monthly rent payment of {fixed_monthly_rent_payment_usd:.2f}"
        )
        return

    investment_monthly_contribution_while_renting_usd = (
        profile.investable_monthly_budget_usd - fixed_monthly_rent_payment_usd
    )
    investment_monthly_contribution_while_owning_usd = (
        profile.investable_monthly_budget_usd - fixed_monthly_property_payment_usd
    )

    profile.investment.update_balance(-profile.rental.initial_payment_usd())
    profile.investment.set_monthly_contribution_usd(
        investment_monthly_contribution_while_renting_usd
    )

    current_month = 0
    investment_tax_liability = 0

    iteration_details: List[IterationDetail] = []

    while current_month <= planning_horizon:

        current_iteration = IterationDetail(month=current_month)

        logger.debug(f"Processing month: {current_month}")
        if current_month == purchase_month:
            initial_property_payment = profile.target_property.initial_payment(profile.mortgage)

            logger.debug(f"{current_month} is property purchase month.")
            logger.debug(
                f"\tInvestment balance of {profile.investment.balance_usd:.2f} reduced by the initial property payment of {initial_property_payment:.2f}"
            )
            logger.debug(
                f"\tMontly investment contribution changed from {profile.investment.monthly_contribution_usd:.2f} to {investment_monthly_contribution_while_owning_usd:.2f}"
            )

            profile.investment.update_balance(-initial_property_payment)
            profile.investment.set_monthly_contribution_usd(
                investment_monthly_contribution_while_owning_usd
            )

        if current_month >= purchase_month:
            current_month_principal = profile.mortgage.current_principal_payment()
            profile.mortgage.update_paid_principal_usd(current_month_principal)

            current_iteration.property_value_usd = profile.target_property.current_value(
                current_month - purchase_month
            )
            current_iteration.remaining_loan_usd = profile.mortgage.remaining_balance()

            current_iteration.property_net_profit_usd = current_iteration.property_value_usd - current_iteration.remaining_loan_usd

        investment_return = profile.investment.calculate_monthly_added_value()
        profile.investment.apply_monthly_return(investment_return, apply_tax=False)
        investment_tax_liability += investment_return.tax_liability_usd

        current_iteration.investment_balance_usd = profile.investment.balance_usd

        # if current_month > 0 and current_month % 11 == 0:
        #     profile.investment.update_balance(-investment_tax_liability)

        iteration_details.append(current_iteration)

        current_month += 1

    return iteration_details