import requests
import time

portfolio = {
    'BTC': 1.5,  # Amount of Bitcoin you own
    'ETH': 26,  # Amount of Ethereum you own
    # Add more cryptocurrencies here
}

# Note some tokens aren't available on Coinbase
def get_crypto_price(ticker):
    url = f'https://api.coinbase.com/v2/prices/{ticker}-USD/spot'
    response = requests.get(url)
    data = response.json()
    return float(data['data']['amount'])

def display_portfolio(portfolio):
    print(f"----------------------------------------------------------\n")
    total_value = 0.0
    for ticker, amount in portfolio.items():
        price = get_crypto_price(ticker)
        value = amount * price
        total_value += value
        print(f"{ticker}: ${price:.2f} (You own {amount} {ticker}, Value: ${value:.2f})")
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    while True:
        display_portfolio(portfolio)
        time.sleep(30)

if __name__ == "__main__":
    main()
