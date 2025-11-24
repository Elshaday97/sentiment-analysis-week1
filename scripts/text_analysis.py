import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def calculate_sentiment(headlines: pd.Series) -> pd.Series:
    """
    Vectorized VADER sentiment for financial headlines
    Input: pandas Series of strings
    Output: pandas Series of compound scores (-1 to +1)
    """
    if headlines.empty:
        print("Please pass headlines to process sentiment")
        return pd.Series([], dtype=float)

    try:
        sid = SentimentIntensityAnalyzer()
        return headlines.apply(lambda text: sid.polarity_scores(text)["compound"])
    except Exception as e:
        print(f"Unable to process sentiments: {e}")
