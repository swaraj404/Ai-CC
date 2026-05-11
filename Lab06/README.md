# Lab06 — Stock Expert System

This folder contains a simple command-line stock expert system in `stockExpertSystem.py`.

## What it does
- Fetches stock data using `yfinance`
- Compares the current price with the 50-day moving average
- Makes a basic `BUY`, `SELL`, or `HOLD` decision
- Saves analyzed results to `expert_report.csv`

## Requirements
- Python 3.10+
- `pandas`
- `yfinance`

## Run instructions
From the `Lab06` folder:

```bash
cd Lab06
python stockExpertSystem.py
```

If you are using the configured virtual environment for this workspace, run:

```bash
/home/swaraj/myenv/bin/python stockExpertSystem.py
```

## Menu options
- `1` — Analyze a stock and save the result to CSV
- `2` — View the saved CSV report
- `3` — Clear the CSV file
- `4` — Exit

## Example ticker symbols
- `TSLA`
- `RELIANCE.NS`
- `AAPL`

## Output file
- `expert_report.csv` is created in the same folder after you save a result.

## Notes
- Make sure your Python environment has `pandas` and `yfinance` installed.
- If you do not see the imports resolve in VS Code, select the Python interpreter at `/home/swaraj/myenv/bin/python`.
