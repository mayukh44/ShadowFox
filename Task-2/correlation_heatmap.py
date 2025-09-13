import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df):
    corr = df[['pm2_5', 'pm10', 'no2', 'so2', 'co', 'o3', 'nh3']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Pollutants')
    plt.show()
