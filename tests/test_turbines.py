from os import path
from unittest import TestCase
import pandas as pd
import numpy as np


filepath = path.split(path.dirname(__file__))[0]

def test_data_loader(data_loader):

    df = data_loader.load_data(filepath=path.join(filepath, "data/turbine_metadata.csv"))

    assert len(df)!= 0 

def test_data_loader_exception(data_loader):

    with TestCase().assertRaises(FileNotFoundError):

        data_loader.load_data(filepath="turbine_metadata.csv")

def test_downtime_analysis(downtime_analysis):

    df = downtime_analysis.downtime_data(path_to_data=path.join(filepath, "data/new_downtime.csv"))

    assert "downtime" in df.columns

def test_vibration_analysis(vibration_analysis):

    df = vibration_analysis.vib_data(path_to_data=path.join(filepath, "data/time_series_all.csv"))

    assert "MeanRadialVib" in df.columns

def test_turbine_status_ok(vibration_analysis):

    test_df = pd.DataFrame(
        {
            "Datetime": ["2022-12-01 00:00:00"],
            "InverterTemp": [30.0],
            "Windspeed": [9.0],
            "CoolantTemp": [30.0],
            "CoolentPressure": [14.0],
            "RadialVibX": [0.2],
            "RadialVibY": [0.22],
            "ActivePower": [15.0],
            "ReactivePower": [16.0],
            "id": [3057],
            "name": ["ABCD"],
            "wind_farm": ["Aplha"],
            "MeanRadialVib": [0.21]
        }
    )

    df = vibration_analysis.turbine_status(df=test_df)

    assert "Status" in df.columns
    assert df["Status"].values[0] == "OK"

def test_turbine_status_warning(vibration_analysis):

    test_df = pd.DataFrame(
        {
            "Datetime": ["2022-12-01 00:00:00"],
            "InverterTemp": [30.0],
            "Windspeed": [9.0],
            "CoolantTemp": [30.0],
            "CoolentPressure": [14.0],
            "RadialVibX": [0.3],
            "RadialVibY": [0.31],
            "ActivePower": [15.0],
            "ReactivePower": [16.0],
            "id": [3057],
            "name": ["ABCD"],
            "wind_farm": ["Aplha"],
            "MeanRadialVib": [0.305]
        }
    )

    df = vibration_analysis.turbine_status(df=test_df)

    assert "Status" in df.columns
    assert df["Status"].values[0] == "WARNING"

def test_turbine_status_down(vibration_analysis):

    test_df = pd.DataFrame(
        {
            "Datetime": ["2022-12-01 00:00:00"],
            "InverterTemp": [30.0],
            "Windspeed": [9.0],
            "CoolantTemp": [30.0],
            "CoolentPressure": [14.0],
            "RadialVibX": [0.0],
            "RadialVibY": [0.0],
            "ActivePower": [15.0],
            "ReactivePower": [16.0],
            "id": [3057],
            "name": ["ABCD"],
            "wind_farm": ["Aplha"],
            "MeanRadialVib": [0.0]
        }
    )

    df = vibration_analysis.turbine_status(df=test_df)

    assert "Status" in df.columns
    assert df["Status"].values[0] == "DOWN"

def test_turbine_status_missing(vibration_analysis):

    test_df = pd.DataFrame(
        {
            "Datetime": ["2022-12-01 00:00:00"],
            "InverterTemp": [30.0],
            "Windspeed": [9.0],
            "CoolantTemp": [30.0],
            "CoolentPressure": [14.0],
            "RadialVibX": [np.nan],
            "RadialVibY": [np.nan],
            "ActivePower": [15.0],
            "ReactivePower": [16.0],
            "id": [3057],
            "name": ["ABCD"],
            "wind_farm": ["Aplha"],
            "MeanRadialVib": [np.nan]
        }
    )

    df = vibration_analysis.turbine_status(df=test_df)

    assert "Status" in df.columns
    assert df["Status"].values[0] == "MISSING DATA"
