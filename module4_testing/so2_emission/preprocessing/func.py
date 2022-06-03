import numpy as np
import pandas as pd


def my_max(x):
    return np.max(x)


def my_min(x):
    return np.min(x)

def row_is_valid(row) -> bool:
    """return True is row is a valid entry"""
    return

def row_to_list(row: str) -> list:
    """ convert a row to a list"""
    return

def merge_table(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """ Merge two Pandas DataFrame with different time series keys

    Parameters
    ----------
    df1
    df2

    Returns
    -------
    df

    """
    return