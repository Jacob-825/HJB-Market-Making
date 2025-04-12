import matplotlib.pyplot as plt
from SimulateOrderbook import simulate_price
from MarketMaker import market_maker

T = 1000  #Time steps
S0 = 100  #Initial mid-price
sigma = 0.5  #Volatility
kappa = 0.1  #Inventory penalty
alpha = 0.02  #Nonlinear inventory impact

S = simulate_price(T, S0, sigma)
bid_prices, ask_prices, inventory = market_maker(S, alpha, kappa)

plt.figure(figsize=(10, 5))
plt.plot(S, label="Mid-Price", color='black')
plt.plot(bid_prices, label="Bid Price", linestyle='dashed')
plt.plot(ask_prices, label="Ask Price", linestyle='dashed')
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()

plt.figure(figsize=(10, 3))
plt.plot(inventory, label="Inventory", color='red')
plt.xlabel("Time")
plt.ylabel("Inventory")
plt.legend()
plt.show()