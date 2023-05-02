from typing import List
import matplotlib.pyplot as plt

def plot_time_series(x: List[float], y: List[float], id: int, upper_cut_off: float = 0.3, lower_cut_off: float = 0.17) -> None:
    """
    function for plotting time series data. For turbine data, x axis is Datetime and y axis is radial vibration

    Arguments:
        x: float. List of x coordinates for plot
        y: float. List of y coordinates for plot
        id: int. Turbine ID to add to plot label.
 
    """

    plt.plot(x, y, label=id, color="blue")
    plt.plot(x, y, color="black", marker=".", linestyle="")
    plt.axhline(y=upper_cut_off, color="red", linestyle="--", label="Upper Warning") # add line to indicate warning for increase in vibrations
    plt.axhline(y=lower_cut_off, color="red", linestyle="dashdot", label="Lower Warning") # add line to indicate warning for increase in vibrations
    plt.xlabel("Date in Dec-2022")
    plt.ylabel("Mean Radial Vibration per Day")
    plt.title("Date vs Radial Vibration per Day for December 2022")
    plt.legend(title="Trubine ID")
    plt.show()
