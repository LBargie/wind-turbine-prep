from typing import List
from .data_loader import TurbineDataLoader
import pandas as pd
import numpy as np

class VibrationAnalysis:

    def __init__(self, data_loader: TurbineDataLoader = None):

        self.loader = data_loader or TurbineDataLoader()

    def vib_data(self, path_to_data: str) -> pd.DataFrame:

        df = self.loader.load_data(filepath=path_to_data, parse_dates=["Datetime"], infer_datetime_format=True)

        # average the X and Y radial vibration columns and add the result as a new column
        df = df.assign(MeanRadialVib=self.avg_radial_vib(df["RadialVibX"].values, df["RadialVibY"].values))

        return df
    
    def vib_data_per_day(self, df: pd.DataFrame) -> pd.DataFrame:

        # group the time series data by day
        return df.groupby(["id", df["Datetime"].dt.day])["MeanRadialVib"].mean().reset_index()
    
    def turbine_status(self, df: pd.DataFrame, upper_cutoff: float = 0.3, lower_cutoff: float = 0.17) -> pd.DataFrame:

        # adding an arbitrary cut-off values based on looking at the plots. This would likely be determined statistically in production.
        conditions = [
            ((df["MeanRadialVib"] <= lower_cutoff) & (df["MeanRadialVib"] > 0.0)),
            df["MeanRadialVib"] >= upper_cutoff,
            df["MeanRadialVib"] == 0.0, 
            df["MeanRadialVib"].isna()
            ]

        # data is missing from some of the time series data so adding status "missing data" for those cases
        results = ["WARNING", "WARNING", "DOWN", "MISSING DATA"]

        return df.assign(Status=np.select(conditions, results, default="OK"))
    
    def avg_radial_vib(self, radialvibx: List[float], radialviby: List[float]) -> List[float]:

        return np.mean([radialvibx, radialviby], axis=0)
