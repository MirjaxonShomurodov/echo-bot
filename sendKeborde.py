import os
import requests
from getUpdetes import get_updetes
TOKEN="6333225235:AAFbjxLb1QS7zZIW4maMZ4-CtRNybDdH6ys"

def doc_url():
        url = "https://random.dog/woof.json"
        respons = requests.get(url)
        return respons.json()['url']


def cat_url():
        url = "https://api.thecatapi.com/v1/images/search"
        respons = requests.get(url)
        return respons.json()[0]['url']
 

def sendMessage(chat_id:str, text:str):
    button1 = {
        "text": "Dog 🐶"
    }
    button2 = {
        "text": "Cat 😺"
    }
    keyboard = {"keyboard": [[button1, button2]], "resize_keyboard": True}
    params = {
        "chat_id":chat_id,
        "text": text,
        "reply_markup": keyboard
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url, json=params)

    return response.json()

def sendPhoto(chat_id:str,photo_url:str):
    params = {
        "chat_id":chat_id,
        "photo":photo_url
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    response = requests.post(url, params=params)
    return response.json()

updates = get_updetes(TOKEN)
chat_id = updates["message"]["chat"]["id"]
text = updates["message"]["text"]

if text == "Dog 🐶":
    sendPhoto(chat_id, photo_url=doc_url())
if text == "Cat 😺 ":
    sendPhoto(chat_id, photo_url=cat_url())
# print(text)