
# Cryptocurrency Portfolio Tracker

This project allows you to track the real-time value of your cryptocurrency portfolio. It uses the CoinGecko API to fetch current prices of cryptocurrencies and calculates the total value of your portfolio. The results are then saved in an Excel file.

## Prerequisites

- Python 3
- Python packages:
  - `csv`
  - `requests`
  - `pandas`

## How to Use

1. Ensure you have a `portfolio.csv` file in the same directory as the script. This file should have the following structure:

    ```
    ticker,amount
    btc,0.5
    eth,2
    ```

    Where "ticker" is the cryptocurrency symbol (e.g., "btc" for Bitcoin) and "amount" is the quantity you own.

2. Run the Python script:

    ```bash
    python script_name.py
    ```

3. Once the script completes, you will find an Excel file in the `output/` directory with the current date and time as the filename. This file will contain details of your portfolio, including the total value.

## Notes

- The script takes a 15-second pause between each request to the CoinGecko API to avoid rate limits.
- Ensure you have a stable internet connection when running the script since it connects to the external CoinGecko API.

## License

This project is distributed under the MIT license. You are free to use, modify, and redistribute it.
