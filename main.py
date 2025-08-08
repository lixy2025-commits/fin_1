from data_fetcher import fetch_stock_data
from indicator_calculator import add_sma
from visualizer import show_data_with_sma
import config

def main():
    """
    Main function to run the stock analysis pipeline.
    """
    (
        fetch_stock_data(config.TICKER, config.START_DATE)
        .pipe(add_sma, period=config.SMA_WINDOW)
        .pipe(show_data_with_sma, period=config.SMA_WINDOW)
    )

if __name__ == "__main__":
    main()
