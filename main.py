import requests
from call import callFromTwilio
import time

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    return response.json()['ethereum']['usd']

def check_price(price, target, up = True):
    if up:
        return price >= target
    else:
        return price <= target
    
def main():
    target_price = 1842.00
    up = False
    while True:
        eth_price = get_eth_price()
        print(f"Current ETH price: {eth_price}")
        
        if check_price(eth_price, target_price, up):
            print("Target price reached!")
            callFromTwilio()
            break
        else:
            print("Target price not reached.")
        
        time.sleep(30)  


if __name__ == "__main__":
    main()
