import matplotlib.pyplot as plt

def seasonal_analysis(df):
    monthly = df.groupby('month')[['pm2_5', 'pm10']].mean()
    monthly.plot(kind='bar')
    plt.title('Monthly PM2.5 & PM10 Averages')
    plt.show()
