from turbines.vibrations import VibrationAnalysis

def main():

    vib = VibrationAnalysis()

    df = vib.vib_data(path_to_data="../data/time_series_all.csv")

    return vib.turbine_status(df=df)

if __name__=="__main__":
    
    # ask for timestamp
    timestamp = input("please submit a timestamp of interest: ")

    # ask for wind farm name
    windfarm = input("Please submit the wind farm name of interest: ")

    status = main()

    result = status[(status["wind_farm"] == windfarm) & (status["Datetime"] == timestamp)]

    print(result[["Datetime", "id", "name", "wind_farm", "Status"]])
    