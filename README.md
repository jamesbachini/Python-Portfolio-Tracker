# Python Crypto Portfolio Tracker

This is a Python script that tracks the real-time value of your cryptocurrency portfolio using the Coinbase API. The script fetches the current prices of specified cryptocurrencies and calculates the total portfolio value based on the amount of each cryptocurrency you own.

Full tutorial here: https://jamesbachini.com/building-a-portfolio-tracker-in-python/

## Features

- Tracks multiple cryptocurrencies in real-time
- Fetches current prices from the Coinbase API
- Calculates and displays the individual and total portfolio values
- Updates every 30 seconds

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

1. Clone the repository or download the `portfolio.py` file.
2. Open the `portfolio.py` file and update the `portfolio` dictionary with your cryptocurrency holdings.
    ```python
    portfolio = {
        'BTC': 1.5,  # Amount of Bitcoin you own
        'ETH': 26,  # Amount of Ethereum you own
        # Add more cryptocurrencies here
    }
    ```
3. Run the script:
    ```bash
    python portfolio.py
    ```

## Example

If you have 1.5 BTC and 26 ETH, the script will output the current prices of BTC and ETH, calculate their individual values based on your holdings, and display the total portfolio value. The output will be updated every 30 seconds.

```bash
Bitcoin (BTC): $40000.00 (You own 1.5 BTC, Value: $60000.00)
Ethereum (ETH): $2500.00 (You own 26 ETH, Value: $65000.00)
Total Portfolio Value: $125000.00
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improving this script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Socials

- [Website](https://jamesbachini.com)
- [YouTube](https://www.youtube.com/c/JamesBachini?sub_confirmation=1)
- [Substack](https://bachini.substack.com)
- [Podcast](https://podcasters.spotify.com/pod/show/jamesbachini)
- [Spotify](https://open.spotify.com/show/2N0D9nvdxoe9rY3jxE4nOZ)
- [Twitter](https://twitter.com/james_bachini)
- [LinkedIn](https://www.linkedin.com/in/james-bachini/)
- [GitHub](https://github.com/jamesbachini)
