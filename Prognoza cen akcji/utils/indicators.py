
import pandas as pd

def add_SMA(df, window=20):
    df[f"SMA_{window}"] = df["Close"].rolling(window=window).mean()
    return df

def add_EMA(df, window=20):
    df[f"EMA_{window}"] = df["Close"].ewm(span=window, adjust=False).mean()
    return df

def add_RSI(df, window=14):
    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df
