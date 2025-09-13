import matplotlib.pyplot as plt
import seaborn as sns

def pollutant_distribution(df):
    for pollutant in ['pm2_5', 'pm10', 'no2', 'so2', 'co', 'o3', 'nh3']:
        plt.figure(figsize=(8,4))
        sns.histplot(df[pollutant], bins=40, kde=True)
        plt.title(f'Distribution of {pollutant.upper()}')
        plt.show()
