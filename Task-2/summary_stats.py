def summary_stats(df):
    print(df.describe())
    print(df[['pm2_5', 'pm10', 'no2', 'so2', 'co', 'o3', 'nh3']].describe())
