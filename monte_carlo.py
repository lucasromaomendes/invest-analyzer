import numpy as np

def monte_carlo_simulation(prices, num_simulations=1000, num_days=120):
    last_price = prices[-1]
    returns = prices.pct_change().dropna()
    mean = returns.mean()
    std_dev = returns.std()

    simulations = np.zeros((num_simulations, num_days))

    for i in range(num_simulations):
        price_series = [last_price]
        for _ in range(num_days):
            price = price_series[-1] * (1 + np.random.normal(mean, std_dev))
            price_series.append(price)
        simulations[i] = price_series[1:]

    return simulations
