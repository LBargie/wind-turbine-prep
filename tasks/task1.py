from turbines.downtime import DowntimeAnalysis

def main():

    downtime = DowntimeAnalysis()

    data = downtime.downtime_data(path_to_data="../data/new_downtime.csv")

    return downtime.downtime_by_windfarm(data)

if __name__=="__main__":

    by_wind_farm = main()
    print("Total downtime across all turbines:", by_wind_farm.sum())
    print(by_wind_farm)
