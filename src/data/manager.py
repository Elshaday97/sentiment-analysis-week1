import pandas as pd
import pathlib as Path
from typing import List


# Methods here are specific to the assignment requirements and not general-purpose
class DataManager:
    TICKERS: List[str] = ["AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA"]

    def __init__(self, data_dir="../data"):
        self.data_dir = Path.Path(data_dir)

    def load_news_data(self, load_processed: bool = False) -> pd.DataFrame:
        if load_processed:
            news_file = self.data_dir / "processed_data" / "processed_news.csv"
        else:
            news_file = self.data_dir / "raw_analyst_ratings.csv"

        if not news_file.exists():
            raise FileNotFoundError(f"News data file not found: {news_file}")

        try:
            print(f"Loading news data from {news_file}")
            df = pd.read_csv(news_file)
            print("News data loaded successfully.")
            return df
        except Exception as e:
            print(f"Error loading news data: {e}")
            raise Exception(f"Failed to load news data: {e}")

    def load_stock(self, ticker: str, load_processed: bool = False) -> pd.DataFrame:
        ticker = ticker.upper()
        if load_processed:
            stock_file = self.data_dir / "processed_data" / f"processed_{ticker}.csv"
        else:
            stock_file = self.data_dir / "finance_data" / f"{ticker}.csv"

        if not stock_file.exists():
            raise FileNotFoundError(
                f"Stock data file not found for ticker {ticker}: {stock_file}"
            )
        try:
            print(f"Loading stock data for {ticker} from {stock_file}")
            if load_processed:
                df = pd.read_csv(stock_file, index_col="Date")
            else:
                df = pd.read_csv(stock_file)

            print(f"Stock data for {ticker} loaded successfully.")
            return df
        except Exception as e:
            print(f"Error loading stock data for {ticker}: {e}")
            raise Exception(f"Failed to load stock data for {ticker}: {e}")

    def load_all_stocks(self, load_processed: bool = False) -> dict:
        results = {}
        failed = []

        for ticker in self.TICKERS:
            try:
                results[ticker] = self.load_stock(ticker, load_processed)
            except Exception as e:
                failed.append(ticker)
                print(f"Failed to load data for {ticker}: {e}")

        if failed:
            print(f"Failed to load data for tickers: {', '.join(failed)}")
        else:
            print("All stock data loaded successfully.")

        return results

    def save_processed_data_to_csv(
        self,
        df: pd.DataFrame,
        fileName: str,
        keep_index=False,
    ):
        try:
            path = self.data_dir / "processed_data" / f"{fileName}.csv"
            if "Unnamed: 0" in df.columns:
                df.drop(columns=["Unnamed: 0"], inplace=True)
            df.to_csv(path, index=keep_index)
            print(f"Successfully saved file to {path}")
        except Exception as e:
            print(f"Error while saving data for {path}: {e}")
