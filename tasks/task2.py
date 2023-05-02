from turbines.vibrations import VibrationAnalysis
from turbines.time_series_plot import plot_time_series

def main():
        
    vibrations = VibrationAnalysis()

    df = vibrations.vib_data(path_to_data="../data/time_series_all.csv")

    return vibrations.vib_data_per_day(df=df)

if __name__ == "__main__":
      
    df = main()

    # specify turbine ID for plotting
    turbine_id = 3057

    # filter data for turbine ID
    for_plot = df[df["id"] == turbine_id]

    plot_time_series(x=for_plot["Datetime"].values, y=for_plot["MeanRadialVib"].values, id=turbine_id)
