def preprocess_data(df):
    df['month'] = df['date'].dt.month
    df['hour'] = df['date'].dt.hour
    df = df.dropna()   # Removes missing values
    return df
