from pandas import DataFrame

def add_sma(df: DataFrame, period: int) -> DataFrame:
    """
    Adds a Simple Moving Average (SMA) column to the DataFrame.

    Args:
        df (DataFrame): The input DataFrame with a 'close' column.
        period (int): The window period for the SMA calculation.

    Returns:
        DataFrame: The DataFrame with an added 'SMA_{period}' column.
    """
    df[f'SMA_{period}'] = df['close'].rolling(window=period).mean()
    return df
