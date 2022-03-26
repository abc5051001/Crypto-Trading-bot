import requests
import json
import time

# while True :
#     response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")
#     data = response.json()
#     currency = data["data"]["base"]
#     price = data["data"]["amount"]
#     print(f"Currency : {currency}  Price: {price}")
#     time.sleep(5)
while True:
    url = "https://api.exchange.coinbase.com/products/ETH-USD/stats"

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    time.sleep(60)
