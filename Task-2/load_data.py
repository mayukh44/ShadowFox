import pandas as pd

def load_data(filename='delhiaqi.csv'):
    df = pd.read_csv(filename, parse_dates=['date'])
    print(df.head())
    return df
