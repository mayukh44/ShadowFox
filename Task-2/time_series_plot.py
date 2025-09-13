import matplotlib.pyplot as plt

def time_series_plot(df):
    plt.figure(figsize=(16,6))
    plt.plot(df['date'], df['pm2_5'], label='PM2.5')
    plt.plot(df['date'], df['pm10'], label='PM10')
    plt.legend()
    plt.title("PM2.5 and PM10 over Time")
    plt.xlabel("Date")
    plt.ylabel("Concentration")
    plt.show()
