import numpy as np
# TODO - random sim for now, import prices later on, MM logic has priority
def simulate_price(T, S0, sigma):
    np.random.seed(42)
    S = np.zeros(T)
    S[0] = S0
    for t in range(1, T):
        dS = sigma * np.random.randn()
        S[t] = S[t-1] + dS
    return S


import pandas as pd

data_events = pd.read_csv("events.csv")
data_games = pd.read_csv("games.csv")

data_events.groupby("game_id").

