"""
    working with requests package
    https://docs.coincap.io/
    
    https://docs.coincap.io/
    https://www.coingecko.com/en/api

    # free proxy sites
    https://spys.one/en/free-proxy-list/
    https://proxyscrape.com/free-proxy-list
    https://free-proxy-list.net/

"""
import requests
import time


def main2():
    def inform_bahman():
        print('hi there.price is good')
    
    my_good_price=80000

    while True:
        response=requests.get("https://api.coincap.io/v2/assets/bitcoin")
        price=float(response.json()['data']['priceUsd'])

        if price <my_good_price:
            inform_bahman()
        else:
            print("price is not good for you:",price)
        
        time.sleep(100)



if __name__ == "__main__":
    # main()
    # main2()
    pass


def main():
    proxies={
        'http':'188.166.230.109:31028',
        'https':'43.153.16.149:13001'
    }

    # r=requests.get("https://google.com")
    # r=requests.get("https://api.coincap.io/v2/assets")
    # r=requests.get("https://api.coincap.io/v2/assets/bitcoin",proxies=proxies,timeout=5)
    # r=requests.get("https://api.coincap.io/v2/assets/bitcoin",proxies={
    #     'https':'socks5://127.0.0.1:1080'
    # })
    r=requests.get("https://api.coincap.io/v2/assets/bitcoin")

    # print(r)
    # print(r.text)

    print("-"*75)

    # price=r.json()
    # print("BTC price now is: ",price['data']['priceUsd'])

    price=r.json()['data']['priceUsd'] # ==>still price is str
    # print("BTC price now is: {:.2f}".format(float(price)))
    # print("BTC price now is:", round(float(price), 2))
    print(f"BTC price now is: {float(price):.2f}")

    