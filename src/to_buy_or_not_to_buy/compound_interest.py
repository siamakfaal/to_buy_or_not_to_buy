import logging

from src.to_buy_or_not_to_buy.helpers.logger import create_logger
from src.to_buy_or_not_to_buy.helpers.plots import plot_wealth_over_iterations
from src.to_buy_or_not_to_buy.types.investment import Investment, InvestmentParameters
from src.to_buy_or_not_to_buy.types.variables import IterationDetail


def main():
    logger = create_logger(name="projected_wealth", level=logging.DEBUG)

    investment_params = InvestmentParameters(
        balance_usd=100_000.00,
        interest_yearly_percent=15.00,
        monthly_contribution_usd=200.00,
        tax_yearly_percent=10.00,
    )

    investment = Investment(investment_params, logger)

    years = 5

    iter_details: List[IterationDetail] = []

    for month in range(years * 12 + 1):
        iter_details.append(
            IterationDetail(month=month, investment_balance_usd=investment.balance_usd)
        )
        monthly_value = investment.calculate_monthly_added_value()
        investment.apply_monthly_return(monthly_value, apply_tax=False)

    plot_wealth_over_iterations(iter_details)


if __name__ == "__main__":
    main()
