# Stock Price Trends

A Python project for analyzing historical stock price movements, computing portfolio risk/return metrics, detecting simple market-pattern signals, and generating actionable recommendations.

## Features

- Loads market data from CSV (`Date, StockA, StockB, StockC, ...`)
- Computes percentage-change based returns
- Falls back to absolute differences if return data is sparse
- Calculates:
  - equal-weight portfolio allocation
  - expected portfolio return
  - portfolio volatility (risk)
- Runs a lightweight pattern detection model
- Generates recommendation text based on risk and detected pattern
- Saves a line chart of stock trends to `output/stock_price_trends.png`

## Project Structure

```text
.
|-- app.py
|-- requirements.txt
|-- README.md
|-- data/
|   `-- sample_market_data.csv
|-- output/
|   `-- stock_price_trends.png
`-- src/
    |-- bias_detection.py
    |-- data_loader.py
    |-- portfolio_optimizer.py
    |-- recommendation_system.py
    `-- visualization.py
```

## Requirements

- Python 3.9+
- pip

Dependencies (also listed in `requirements.txt`):

- pandas
- numpy
- scikit-learn
- matplotlib

## Quick Start

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

## Input Data Format

The main CSV should include a `Date` column followed by one or more stock columns:

```csv
Date,StockA,StockB,StockC
1/1/2023,100,120,90
1/2/2023,101,119,92
...
```

## Output

When executed, the app prints:

- Portfolio allocation weights
- Expected return
- Portfolio volatility
- Pattern detection result
- Investment recommendation

It also saves a chart at:

- `output/stock_price_trends.png`

## Notes

- The current optimizer uses equal weighting as a baseline implementation.
- You can replace this logic in `src/portfolio_optimizer.py` with advanced optimization methods.

## License

This project is currently unlicensed. Add a license file if you plan to distribute it publicly.
