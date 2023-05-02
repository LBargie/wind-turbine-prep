import pandas as pd


class TurbineDataLoader:

    # could add more methods for fetching data from S3 or a database, for example. 
    # Or define a "DataLoader" abstract base class and have csv, S3 and/or database sub-classes.

    def load_data(self, filepath: str, **kwargs) -> pd.DataFrame:
        """
        wrapper method for .read_csv()

        Arguments:
            filepath: str. The path name for the file to be read.
            kwargs: key word arguments belonging to .read_csv()

        Returns:
            Pandas dataframe
        """
        return pd.read_csv(filepath, low_memory=False, **kwargs)

    