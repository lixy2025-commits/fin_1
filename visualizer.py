import matplotlib.pyplot as plt
from pandas import DataFrame

def show_data_with_sma(df: DataFrame, period: int):
    """
    Displays a plot of the close price and SMA.

    Args:
        df (DataFrame): DataFrame with 'close' and 'SMA_{period}' columns.
        period (int): The SMA period, used for the plot title.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label='Close Price')
    plt.plot(df[f'SMA_{period}'], label=f'{period}-Day SMA')
    plt.title(f'Stock Price with {period}-Day SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()
    return df
