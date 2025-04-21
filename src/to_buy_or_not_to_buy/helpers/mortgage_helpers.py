from src.to_buy_or_not_to_buy.types.variables import Mortgage, OwnedProperty


def mortgage_monthly_payment(mortgage: Mortgage) -> float:
    """
    Calculate the total monthly mortgage payment using the amortization formula.
    """

    if mortgage.paid_principal >= mortgage.initial_loan:
        return 0.0

    monthly_interest_rate = mortgage.interest / 12 / 100
    total_months = mortgage.term * 12

    if monthly_interest_rate == 0:
        return mortgage.initial_loan / total_months

    projected_interest = (1 + monthly_interest_rate) ** total_months
    monthly_payment = (
        mortgage.initial_loan
        * monthly_interest_rate
        * projected_interest
        / (projected_interest - 1)
    )

    return monthly_payment


def current_principal_payment(mortgage: Mortgage) -> float:
    """
    Estimate the principal portion of the upcoming monthly mortgage payment,
    based on the current state of the mortgage.
    """
    total_monthly_payment = mortgage_monthly_payment(mortgage)
    current_balance = remaining_balance(mortgage)
    monthly_interest = current_balance * (mortgage.interest / 100 / 12)
    return max(total_monthly_payment - monthly_interest, 0)


def remaining_balance(mortgage: Mortgage) -> float:
    return max(mortgage.initial_loan - mortgage.paid_principal, 0)
