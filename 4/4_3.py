"""
    working with requests package
    https://docs.coincap.io/
    
    https://docs.coincap.io/
    https://www.coingecko.com/en/api
"""
import requests

def main():
    # r=requests.get("https://google.com")
    # r=requests.get("https://api.coincap.io/v2/assets")
    r=requests.get("https://api.coincap.io/v2/assets/bitcoin")

    print(r)

    print("-"*75)
    # print(r.text)

    # print(r.json())
    price=r.json()
    print(price['data'])
    print("-"*75)
    print("btc price now is: ",price['data']['priceUsd'])


if __name__ == "__main__":
    main()