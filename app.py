from src.data_loader import load_data
from src.portfolio_optimizer import optimize_portfolio
from src.recommendation_system import recommend_action
from src.visualization import plot_prices
from src.bias_detection import train_bias_model, detect_bias

import os
import numpy as np

PROJECT_NAME = "Stock Price Trends"

# Load data
data = load_data("data/sample_market_data.csv")

returns_df = data.iloc[:,1:].pct_change()
returns_df = returns_df.replace([np.inf, -np.inf], np.nan).dropna()

# Fallback for sparse periods where percentage change may be undefined.
if returns_df.empty:
	returns_df = data.iloc[:,1:].diff().dropna()

if returns_df.empty:
	raise ValueError("Not enough time-series points to compute risk metrics.")

returns = returns_df.values

weights, portfolio_return, portfolio_risk = optimize_portfolio(returns)

print(f"{PROJECT_NAME}")
print("Optimal Portfolio Allocation Weights:", weights)
print("Expected Return:", portfolio_return)
print("Portfolio Volatility:", portfolio_risk)

# Fake bias training data
X = np.array([[1,0],[0,1],[1,1],[0,0]])
y = np.array([1,0,1,0])

model = train_bias_model(X,y)

bias = detect_bias(model,[1,0])

print("Pattern Detection:", bias)

recommendation = recommend_action(portfolio_risk,bias)

print("Investment Recommendation:", recommendation)

chart_path = plot_prices(data, show_plot=True)
print("Stock trend chart saved at:", chart_path)