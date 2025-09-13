import matplotlib.pyplot as plt

def hourly_analysis(df):
    hourly = df.groupby('hour')[['pm2_5', 'pm10']].mean()
    hourly.plot()
    plt.title('Hourly PM2.5 & PM10 Averages')
    plt.show()
