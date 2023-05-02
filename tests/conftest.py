import pytest
from turbines.data_loader import TurbineDataLoader
from turbines.downtime import DowntimeAnalysis
from turbines.vibrations import VibrationAnalysis

@pytest.fixture()
def data_loader():
    return TurbineDataLoader()

@pytest.fixture()
def downtime_analysis():
    return DowntimeAnalysis()

@pytest.fixture()
def vibration_analysis():
    return VibrationAnalysis()
