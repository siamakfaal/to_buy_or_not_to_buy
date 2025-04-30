from typing import List

import plotly.graph_objects as go

from src.to_buy_or_not_to_buy.types.variables import IterationDetail


def plot_wealth_over_iterations(iteration_details: List[IterationDetail]) -> None:

    months = [detail.month for detail in iteration_details]
    investment_balance = [detail.investment_balance_usd for detail in iteration_details]
    property_net_profit = [detail.property_net_profit_usd for detail in iteration_details]
    net_wealth = [inv + prof for inv, prof in zip(investment_balance, property_net_profit)]

    # Create the plot
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=months, y=investment_balance, mode="lines", name="Investment Balance")
    )
    fig.add_trace(
        go.Scatter(x=months, y=property_net_profit, mode="lines", name="Property Net Profit")
    )
    fig.add_trace(go.Scatter(x=months, y=net_wealth, mode="lines", name="Net Wealth"))

    # Customize layout
    fig.update_layout(
        title="Investment Performance Over Time",
        xaxis_title="Month",
        yaxis_title="USD",
        legend_title="Metrics",
        template="plotly_white",
    )

    # Show plot
    fig.show()
