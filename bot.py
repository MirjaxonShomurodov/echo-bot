import requests
from time import sleep

TOKEN='6418102882:AAG4q3sHxDfBlZM3f3Bi4kjiZOYDUGL908Y'
def getUpdates() -> list:
    URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url=URL)
    updates=response.json()['result']
    return updates

def sendMessage(chat_id:str, text:str):
    params = {
        "chat_id":chat_id,
        "text": text
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    response = requests.get(url, params=params)

def sendPhoto(chat_id:str,photo:str):
    params = {
        "chat_id":chat_id,
        "photo":photo
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    respons = requests.post(url,params=params)
    return respons.json()
def sendDocument(chat_id:str,document:str):
    params = {
        "chat_id":chat_id,
        "document":document
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    respons = requests.post(url,params=params)
    return respons.json()
def sendDice(chat_id, emoji=None):
    params = {
        "chat_id": chat_id,
        "emoji": emoji
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    response = requests.post(URL, params=params)
    return response.json()
def sendContact(chat_id, phone_number,first_name,last_name=None):
    params = {
        "chat_id":chat_id,
        "phone_number":phone_number,
        "first_name":first_name,
        "last_name":last_name
    }
    URL = f"https://api.telegram.org/bot{TOKEN}/sendContact"
    response = requests.post(URL,params=params)
    return response.json()

last_message_id = -1

while True:
    updates = getUpdates()

    message_id = updates[-1]['message']['message_id']

    message  = updates[-1]['message']

    chat_id = updates[-1]['message']['chat']['id']
   
    print(f"MESSAGE ID: {message_id}  LAST MESSAGE ID: {last_message_id}")


    if message_id != last_message_id:
        text = message.get("text")
        photo = message.get("photo")
        document = message.get("document")
        emoji = message.get("emoji")
        phone_number = message.get("phone_number")
        first_name = message.get("first_name")
        last_name = message.get("last_name")
 
        if text !=None:
            if text == "/start":
                sendMessage(chat_id,f"welcome to bot!")
            else:
                sendMessage(chat_id,text)
        elif photo !=None:
            file_id = photo[0]["file_id"]
            sendPhoto(chat_id,file_id)
        elif document !=None:
            file_id = document[0]["file_id"]
            sendDocument(chat_id,file_id)
        elif emoji != None:
            file_id = emoji[0]["file_id"]
            sendDice(chat_id,file_id)
        elif phone_number !=None:
            file_id = phone_number[0]["file_id"]
            file_id = first_name[0]["file_id"]
            file_id = last_name[0]["file_id"]
        else:
            sendMessage(chat_id,emoji)
        
        last_message_id = message_id

    sleep(2)
