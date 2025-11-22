# Sentiment Analysis & Quantitative Finance Week 1

A modular Python project analyzing the relationship between financial news sentiment and stock price movements.

## Key Features

- **Single source of truth** — `DataLoader.TICKERS` used everywhere
- **Professional technical indicators** via chainable `TechnicalIndicators` class
- **Robust data loading** with error handling and logging
- **Portfolio optimization** using PyNance (Max Sharpe & Min Variance)
- **Clean visualizations** and summary tables
- **Auto-reloading** in notebooks for rapid development

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
