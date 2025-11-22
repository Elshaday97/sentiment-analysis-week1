import pandas as pd
import talib


class TechnicalIndicators:
    def __init__(self, df: pd.DataFrame):
        if df.empty or "Close" not in df.columns:
            raise ValueError("Please use a non empty dataframe with Close column")
        self.df = df.copy().sort_index()
        self.closing_price = df["Close"]

    def add_sma(self):
        time_period = 20
        col_name = f"SMA_{time_period}"
        self.df[col_name] = talib.SMA(self.closing_price, timeperiod=time_period)

        print(f"Added {col_name}")
        return self

    def add_ema(self):
        time_period = 20
        col_name = f"EMA_{time_period}"
        self.df[col_name] = talib.EMA(self.closing_price, timeperiod=time_period)

        print(f"Added {col_name}")
        return self

    def add_rsi(self):
        time_period = 14
        col_name = f"RSI_{time_period}"
        self.df[col_name] = talib.RSI(self.closing_price, timeperiod=time_period)

        print(f"Added {col_name}")
        return self

    def add_macd(self, fast=12, slow=26, signal=9):
        macd, macd_signal, macd_hist = talib.MACD(
            self.closing_price, fastperiod=fast, slowperiod=slow, signalperiod=signal
        )

        self.df["MACD"] = macd
        self.df["MACD_Signal"] = macd_signal
        self.df["MACD_Hist"] = macd_hist

        print("Added MACD, MACD Signal, MACD Hist")

        return self

    def add_all_indicators(self):
        self.add_sma().add_ema().add_rsi().add_macd()

        return self

    def get_data(self) -> pd.DataFrame:
        return self.df
