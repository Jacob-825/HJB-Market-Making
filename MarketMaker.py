import numpy as np

def market_maker(S, alpha, kappa):
    q = 0  # Initial inventory
    bid_prices, ask_prices, inventory = [], [], []
    
    for t in range(len(S)):
        spread = 1 + alpha * q**2  # Nonlinear spread adjustment
        bid = S[t] - spread / 2
        ask = S[t] + spread / 2
        
        # Simulated execution: market maker fills orders probabilistically
        if np.random.rand() < 0.5:
            q += 1  # Buy at bid
        if np.random.rand() < 0.5:
            q -= 1  # Sell at ask
        
        # Apply inventory penalty
        q -= kappa * q
        
        bid_prices.append(bid)
        ask_prices.append(ask)
        inventory.append(q)
    
    return bid_prices, ask_prices, inventory