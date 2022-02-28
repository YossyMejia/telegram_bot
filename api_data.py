import requests
import json


def getCoinPrice(coin_id):
    try:
        link = "https://api.coingecko.com/api/v3/coins/"+coin_id.lower()+"/market_chart?" \
                                                                         "vs_currency=usd&days=0&interval=0"
        response = requests.get(link)
        data = json.loads(response.text)
        print(data)
        if("prices" in data):
            # Get the prices in the market information
            data = data['prices']
            # Get the second value of the array, the firts one it's not relevant
            price = data[0][1]
            message = "El precio de la moneda " + coin_id + " en USD es de: " + str(price)
            return message
        else:
            message = "No se ha encontrado informacion sobre la moneda ingresada"
            return message
    except:
        message = "Ha ocurrido un error intentelo nuevamente."
        return message
