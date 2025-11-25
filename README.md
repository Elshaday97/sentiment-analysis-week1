# Sentiment Analysis & Quantitative Finance Week 1

A modular Python project analyzing the relationship between financial news sentiment and stock price movements.

## Current Progress (Nov 22, 2025)

| Task                              | Status      | Details                                                                 |
| --------------------------------- | ----------- | ----------------------------------------------------------------------- |
| Task 1 — News EDA                 | Completed   | Publisher analysis, domain extraction, time trends, headline stats      |
| Task 2 — Quantitative Analysis    | Completed   | TA-Lib indicators (SMA, EMA, RSI, MACD), PyNance portfolio optimization |
| Task 3 — News ↔ Stock Correlation | Completed   | Date alignment & sentiment prep done; correlation in progress           |
| Modular Architecture              | Completed   | Full `src/` package with classes, docstrings, and clean notebooks       |
| Git Workflow                      | Completed   | Branch per task, daily commits, PRs merged                              |

### Key Interim Findings (So Far)

| Area                   | Discovery                                                                        |
| ---------------------- | -------------------------------------------------------------------------------- |
| **News Volume**        | Paul Quintaro has published the most articles                                    |
| **Publication Spikes** | Clear spikes on early mornings, Thursday is when most aricles are published      |
| **Headline Noise**     | Headlines filled with boilerplate that had to be removed along with common words |
| **Technical Signals**  | NVDA consistently shows **RSI > 70** (overbought) + strong MACD bullish cross    |
| **Correlation Analysis**  | All tickers show weak relation among average sentiment and return price       |

## Key Features

- **Single source of truth** — `DataLoader.TICKERS` used everywhere
- **Professional technical indicators** via chainable `TechnicalIndicators` class
- **Robust data loading** with error handling and logging
- **Portfolio optimization** using PyNance (Max Sharpe & Min Variance)
- **Clean visualizations** and summary tables
- **Auto-reloading** in notebooks for rapid development

## Project Structure

```bash

├── src/                  # Reusable, importable package
│   ├── data/             # DataLoader class
│   ├── indicators/       # TechnicalIndicators class (encapsulated TA-Lib)
├── notebooks/            # Clean, high-level analysis & visualization
├── scripts/              # Reusable utility functions
├── data/                 # Data processing
├── requirements.txt
└── README.md
```

## Setup & Run

```bash
# Clone and enter
git clone git@github.com:Elshaday97/sentiment-analysis-week1.git
cd sentiment-analysis-week1

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
# venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

## Tech Stack

- Python 3.10+
- Pandas, NumPy
- TA-Lib (technical indicators)
- PyNance (portfolio optimization)
- Matplotlib, Seaborn
- Scikit-learn, NLTK
- Jupyter Lab
