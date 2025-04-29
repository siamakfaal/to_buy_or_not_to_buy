from dataclasses import dataclass

from .investment import Investment
from .mortgage import Mortgage
from .rental import Rental
from .target_property import TargetProperty


@dataclass
class IterationDetail:
    month: int = 0
    investment_balance_usd: float = 0.00
    property_net_profit_usd: float = 0.00
    property_value_usd: float = 0.00
    remaining_loan_usd: float = 0.00


@dataclass
class InvestmentProfile:
    rental: Rental
    target_property: TargetProperty
    mortgage: Mortgage
    investment: Investment

    investable_monthly_budget_usd: float
