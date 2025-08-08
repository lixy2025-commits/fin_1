from pandas import DataFrame
from openbb import obb


def fetch_stock_data(ticker:str, start_date:str="2025-01-01")-> DataFrame:
    """
    Fetches stock data for a given ticker and start date.
    
    Args:
        ticker (str): The stock ticker symbol.
        start_date (str): The start date in 'YYYY-MM-DD' format.
    
    Returns:
        DataFrame: A DataFrame containing the stock data.
    """
    output = obb.equity.price.historical(
        symbol=ticker,
        start_date=start_date,
        interval="1d",
        output_format="pandas",
        provider='yfinance'
    )
    return output.to_dataframe()

def main():
    from openbb_core.provider.utils.errors import EmptyDataError
    from openbb_core.app.model.abstract.error import OpenBBError
    ticker = "AAPL"
    start_date = "2023-01-01"
    try:
        stock_data = fetch_stock_data(ticker, start_date)
        print(stock_data)
    except (EmptyDataError, OpenBBError) as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
