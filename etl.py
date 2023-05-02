import pandas as pd
import glob
import re

"""
    Script for wrangling the supplied turbine data ready for analysis. To be run before running the task scripts.
    This could be done as part of an AWS pipeline. For example, time series data could be sent to S3 and a Lambda 
    function could be used to forward the data to another bucket or to a database ready for analysis. CSV files can
    also be directly queried by AWS Athena.

    If the files remain in .csv format then you could use something like DuckDB and perform SQL directly on the .csv
    without having to use .read_csv(). In addition, the Ibis package provides a pandas-like API on top of DuckDB if 
    you want to avoid writing SQL queries.
"""

# combine downtime and turbine_metadata for task 1. 
dt = pd.read_csv("downtime.csv", low_memory=False, parse_dates=["start", "end"], infer_datetime_format=True)
meta = pd.read_csv("turbine_metadata.csv", low_memory=False)

# merge downtime data with metadata
dt_meta = dt.merge(meta, how="left", on="id")

# import data. Could be stored in S3. Could use Athena to query files in S3.
files = glob.glob("time_series/*")

# get the turbine ID from the file name
ids = [re.findall("\d+", id) for id in files]

# load the time series data
data = [pd.read_csv(file, low_memory=False, parse_dates=[0], infer_datetime_format=True) for file in files]

# add ID as a column to time series data
id_data = [df.assign(id=i*len(df)) for i, df in zip(ids, data)]

# concatenate all dataframes. Could be saved as a database table. 
time_series = pd.concat(id_data, ignore_index=True).astype({"id": int})

time_series_data = time_series.merge(meta, on="id", how="left")

time_series_all = time_series_data.rename({time_series_data.columns[0]: "Datetime"}, axis=1)

# output dataframes to csv
dt_meta.to_csv("new_downtime.csv", index=False)
time_series_all.to_csv("time_series_all.csv", index=False)
