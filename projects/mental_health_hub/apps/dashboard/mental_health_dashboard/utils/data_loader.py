import pandas as pd

def load_data():
    df = pd.read_csv("data/mock_eldercare_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df
