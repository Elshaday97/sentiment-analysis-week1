# Notebooks

This folder contains **notebooks** used for exploratory data analysis (EDA), prototyping, visualization, and quantitative research.

They are designed to be **interactive** and serve as a sandbox for insights — all reusable logic has been moved to the `src/` package for modularity and testing.

## Current Notebooks

### `news_eda.ipynb`

Exploratory analysis of the financial news dataset (`raw_analyst_ratings.csv`).

**Key analyses:**

- Dataset overview and structure
- Publisher activity and domain extraction
- Publication frequency over time
- Headline length statistics
- Top domains visualization (Seaborn bar plot)

Uses:

- `src.data.DataLoader` for loading news
- `scripts/text_cleaning.py` for domain extraction and text preprocessing

### `ticker_analysis.ipynb`

Quantitative analysis of stock price data for major tech stocks.

**Features:**

- Loads OHLCV data for `AAPL`, `AMZN`, `GOOG`, `META`, `MSFT`, `NVDA`
- Applies technical indicators using `src.indicators.TechnicalIndicators`
  - SMA
  - EMA
  - RSI
  - MACD + Signal + Histogram
  - Bollinger Bands
- Portfolio optimization using **PyNance**
  - Max Sharpe Ratio portfolio
  - Minimum Variance portfolio
- Summary tables with `tabulate`
- Inline visualizations (Matplotlib)

## How to Run

1. Activate your virtual environment:

   ```bash
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

2. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter
   ```bash
    jupyter lab
   ```
