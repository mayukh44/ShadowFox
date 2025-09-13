from load_data import load_data
from preprocess_data import preprocess_data
from summary_stats import summary_stats
from pollutant_distribution import pollutant_distribution
from time_series_plot import time_series_plot
from seasonal_analysis import seasonal_analysis
from hourly_analysis import hourly_analysis
from correlation_heatmap import correlation_heatmap

if __name__ == "__main__":
    df = load_data('delhiaqi.csv')
    df = preprocess_data(df)
    summary_stats(df)
    pollutant_distribution(df)
    time_series_plot(df)
    seasonal_analysis(df)
    hourly_analysis(df)
    correlation_heatmap(df)
