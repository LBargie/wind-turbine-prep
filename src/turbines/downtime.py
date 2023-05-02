from typing import List
import pandas as pd
from .data_loader import TurbineDataLoader
from datetime import datetime, timedelta

class DowntimeAnalysis:

    def __init__(self, data_loader: TurbineDataLoader = None):

        self.loader = data_loader or TurbineDataLoader()

    def downtime_data(self, path_to_data: str) -> pd.DataFrame:

        # load downtime data for analysis
        df = self.loader.load_data(filepath=path_to_data, parse_dates=["start", "end"], infer_datetime_format=True)

        # calculate downtime and add "downtime" column to dataframe
        df = df.assign(downtime=self.downtime_calc(df["start"].values, df["end"].values))

        return df
        
    def downtime_by_windfarm(self, data: pd.DataFrame) -> pd.Series:

        # group dowtime data by wind farm and calculate the sum of the downtime
        return data.groupby("wind_farm")["downtime"].agg("sum")

    def downtime_calc(self, start: List[datetime], end: List[datetime]) -> List[timedelta]:
        
        return end-start
