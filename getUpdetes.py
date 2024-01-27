import requests
def get_updetes(TOKEN):
    BASE_URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    respons = requests.get(url=BASE_URL)
    updetes = respons.json()
    data = updetes["result"][-1]
    return data