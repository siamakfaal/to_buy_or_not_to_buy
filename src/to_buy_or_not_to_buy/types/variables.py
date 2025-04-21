from dataclasses import dataclass


@dataclass
class Rental:
    application_fee: float
    rent: float
    utilities: float
    insurance: float
    commute_cost: float
    gym_subscription: float
    car_payment: float
    car_down_payment: float


@dataclass
class OwnedProperty:
    tax: float
    maintenance: float
    repair: float
    remodeling: float
    utilities: float
    insurance: float
    hoa: float
    appreciation: float
    commute_cost: float
    gym_subscription: float
    car_payment: float
    car_down_payment: float


@dataclass
class Mortgage:
    initial_loan: float
    paid_principal: float
    interest: float
    application_fee: float
    term: float
    closing_cost: float
    down_payment: float


@dataclass
class Investment:
    balance: float
    interest: float
    budget: float
    tax: float


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
