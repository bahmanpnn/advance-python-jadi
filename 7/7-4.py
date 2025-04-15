"""
    working with requests package
    https://docs.coincap.io/
    
    https://docs.coincap.io/
    https://www.coingecko.com/en/api

    # free proxy sites
    https://spys.one/en/free-proxy-list/
    https://proxyscrape.com/free-proxy-list
    https://free-proxy-list.net/

    {'message': 'We are deprecating this version of the CoinCap API on March 31, 2025. Sign up for our new V3 API at https://pro.coincap.io/dashboard'}


"""
import requests
import time


def inform_bahman(my_good_price,price):
    """
        this is for sendin sms and message to user.
        example of sms service provider is kavenegar. 
    """

    API_KEY=""
    url=""

    message=f"price is lower than you want({my_good_price}>{price}).lets buy it!!!"
    payload={'receptor':'09150123456','message':message}

    # send request to sms provider
    response=requests.post(url,data=payload)
    print(response)

def main():

    r=requests.get("")

    # print(r.text)
    # print("-"*75)

    my_good_price=71000
    price=float(r.json())

    if my_good_price > price:
        inform_bahman(my_good_price,price)

    



if __name__ == "__main__":
    main()
    # main2()



















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

