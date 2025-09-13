# Delhi AQI Analysis Project

## Project Overview
This project analyzes Air Quality Index (AQI) data for Delhi using hourly pollutant measurements. It provides statistical insights and visualizations focusing on key pollutants, seasonal and hourly variations, and pollutant correlations. These analyses support public health and environmental policy decisions.

---

## File Descriptions

### 1. `load_data.py`
- **Purpose:** Load the AQI dataset CSV into a pandas DataFrame.
- **Main Function:** `load_data(filename)` — reads CSV and parses dates.
- **Usage:** Use to load raw data before analysis.

### 2. `preprocess_data.py`
- **Purpose:** Preprocesses data, adds month and hour features, and handles missing values.
- **Main Function:** `preprocess_data(df)` — prepares data for analysis.
- **Usage:** Call after loading data.

### 3. `summary_stats.py`
- **Purpose:** Prints descriptive statistics for pollutants.
- **Main Function:** `summary_stats(df)`
- **Usage:** Get an overview of dataset distribution and ranges.

### 4. `pollutant_distribution.py`
- **Purpose:** Plots histograms with KDE for each pollutant.
- **Main Function:** `pollutant_distribution(df)`
- **Usage:** Visualize pollutant concentration distributions.

### 5. `time_series_plot.py`
- **Purpose:** Plots PM2.5 and PM10 trends over time.
- **Main Function:** `time_series_plot(df)`
- **Usage:** Analyze pollutant variations over the dataset period.

### 6. `seasonal_analysis.py`
- **Purpose:** Bar plot of monthly average pollutant concentrations.
- **Main Function:** `seasonal_analysis(df)`
- **Usage:** Understand seasonal effects on pollution levels.

### 7. `hourly_analysis.py`
- **Purpose:** Line plot of hourly average pollutant levels.
- **Main Function:** `hourly_analysis(df)`
- **Usage:** Detect daily patterns or spikes.

### 8. `correlation_heatmap.py`
- **Purpose:** Shows correlation among pollutants via heatmap.
- **Main Function:** `correlation_heatmap(df)`
- **Usage:** Identify relationships between pollutants.

### 9. `main.py`
- **Purpose:** Runs full analysis workflow sequentially.
- **Usage:** Execute to perform complete data loading, preprocessing, and all analyses.

---

## Setup Instructions (Mac + VSCode)

1. Ensure Python 3 is installed:  

2. Open VSCode and create a project folder.

3. Place the dataset `delhiaqi.csv` in the project folder.

4. Open the VSCode terminal and install required libraries:  





---

## Notes

- No CSS files are needed; all visualizations are styled via Python libraries.
- Each plot window appears separately due to individual `plt.show()` calls.
- Modular files allow running or modifying specific parts of the analysis.
- Extendable for machine learning models or advanced time series analysis.

---

## Summary Table

| File Name                 | Purpose                             | Main Function            |
|---------------------------|-----------------------------------|--------------------------|
| `load_data.py`            | Load dataset                      | `load_data(filename)`    |
| `preprocess_data.py`      | Data preprocessing                | `preprocess_data(df)`    |
| `summary_stats.py`        | Display descriptive statistics    | `summary_stats(df)`      |
| `pollutant_distribution.py` | Plot pollutant distributions      | `pollutant_distribution(df)` |
| `time_series_plot.py`     | Plot pollutant time series        | `time_series_plot(df)`   |
| `seasonal_analysis.py`    | Monthly average pollutant analysis| `seasonal_analysis(df)`  |
| `hourly_analysis.py`      | Hourly pollutant trend analysis   | `hourly_analysis(df)`    |
| `correlation_heatmap.py`  | Pollutant correlation heatmap     | `correlation_heatmap(df)`|
| `main.py`                 | Full workflow execution            | Runs all above functions |

---

This README guides new users to easily run and understand the Delhi AQI analysis project.
