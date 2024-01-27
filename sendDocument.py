import os
import requests
from time import sleep
from bot import getUpdates
TOKEN='5839280734:AAEtOVL7UkQbr5yPnaxvV81tVrmwum4mDhA'
def sendDocument(chat_id,document):
    params = {
        "chat_id":chat_id
    }
    files = {
        "document":document
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    respons = requests.post(url,params=params,files=files)
document = open("last.text","rb")
data = getUpdates(TOKEN)
chat_id = ["massage"]["chat"]["id"]
sendDocument(chat_id,document)

# def sendContact(chat_id, phone_number,first_name,last_name=None):
#     params = {
#         "chat_id":chat_id,
#         "phone_number":phone_number,
#         "first_name":first_name,
#         "last_name":last_name
#     }
#     URL = f"https://api.telegram.org/bot{TOKEN}/sendContact"
#     response = requests.post(URL,params=params)
#     return response.json()
# data = get_updetes(TOKEN)
# chat_id = data['message']['chat']['id']
# sendContact(chat_id,"+998884084304","Mirjaxon","SHomurodov")


def sendDice(chat_id, emoji=None):
    params = {
        "chat_id": chat_id,
        "emoji": emoji
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    response = requests.post(URL, params=params)
    return response.json()
chat_id = data['message']['chat']['id']
sendDice(chat_id, emoji="🏀")


def sendDocument(chat_id,document):
    params = {
        "chat_id":chat_id,
        "document":document
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    respons = requests.get(url,params=params)

document = open("last.txt","rb")
chat_id = data['message']['chat']['id']
sendDocument(chat_id, document)