import re
import nltk

nltk.download("stopwords")
ENGLISH_STOP_WORDS = set(nltk.corpus.stopwords.words("english"))

financial_junk = {
    "shares",
    "share",
    "stocks",
    "inc",
    "corp",
    "ltd",
    "co",
    "nasdaq",
    "nyse",
    "benzinga",
    "pro",
    "alert",
    "vs",
    "est",
    "pt",
    "downgrades",
    "upgrades",
    "raises",
    "lowers",
    "reiterates",
    "initiates",
    "maintains",
    "buy",
    "sell",
    "hold",
    "neutral",
    "outperform",
    "market",
    "perform",
    "rating",
    "target",
    "price",
    "week",
    "weeks",
    "high",
    "low",
    "top",
    "mid",
    "mover",
    "watch",
    "recap",
    "earnings",
    "quarter",
    "q1",
    "q2",
    "q3",
    "q4",
    "fiscal",
    "reports",
    "announces",
    "update",
    "news",
    "says",
    "say",
}
stop_words = ENGLISH_STOP_WORDS.union(financial_junk)


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    words = [w for w in words if w not in stop_words]
    text = " ".join(words)

    return text


def extract_domain(publisher):
    if "@" in str(publisher):
        return publisher.split("@")[-1].lower()
    return str(publisher).lower()
