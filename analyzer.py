import numpy as np
import pandas as pd
from monte_carlo import monte_carlo_simulation

def evaluate_assets(price_df):
    results = []
    for ticker in price_df.columns:
        simulations = monte_carlo_simulation(price_df[ticker].dropna())
        expected_return = simulations[:, -1].mean()
        risk = simulations[:, -1].std()
        sharpe = expected_return / risk if risk != 0 else 0
        results.append((ticker, expected_return, risk, sharpe))

    ranked = sorted(results, key=lambda x: x[3], reverse=True)
    return pd.DataFrame(ranked, columns=["Ticker", "Expected Return", "Risk", "Sharpe"]).head(10)
