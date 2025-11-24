import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def calculate_sentiment(headlines: pd.Series) -> pd.Series:
    """
    Computes the compound sentiment score for a series of headlines using
    NLTK's VADER sentiment analyzer.

    Args:
        headlines (pd.Series): A pandas Series containing text headlines.

    Returns:
        pd.Series: A pandas Series of compound sentiment scores ranging from -1
                   (very negative) to 1 (very positive). If the input Series is
                   empty, returns an empty Series of type float.

    Notes:
        Requires NLTK's VADER lexicon. Install and download it via:
        >>> import nltk
        >>> nltk.download('vader_lexicon')

    """

    if headlines.empty:
        print("Please pass headlines to process sentiment")
        return pd.Series([], dtype=float)

    try:
        sid = SentimentIntensityAnalyzer()
        return headlines.apply(lambda text: sid.polarity_scores(text)["compound"])
    except Exception as e:
        print(f"Unable to process sentiments: {e}")
