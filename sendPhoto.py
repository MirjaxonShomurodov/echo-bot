import os
import requests
from time import sleep
from bot import getUpdates
TOKEN='5839280734:AAEtOVL7UkQbr5yPnaxvV81tVrmwum4mDhA'
# def sendPhoto(chat_id:str,photo:str):
#     params = {
#         "chat_id":chat_id
#     }
#     files = {
#         "photo":photo
#     }
#     url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
#     respons = requests.post(url,params=params,files=files)
#     return respons.json()

# photo = open('bot.png','rb')
# photo_url='https://miro.medium.com/v2/resize:fit:300/1*YVTFl1UEkt3_rkez-DIU9w.png'

# data = getUpdates(TOKEN)
# chat_id = data['message']['chat']['id']
# sendPhoto(chat_id, photo)
def sendMessage(chat_id:str, text:str, parse_mode):
    params = {
        "chat_id":chat_id,
        "text": text,
        "parse_mode": parse_mode
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url, params=params)

def sendPhoto(chat_id:str,photo:str):
    params = {
        "chat_id": chat_id,
        "photo": photo
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    response = requests.get(URL, params = params)
    return response.json()

last_message_id = -1

while True:
    updates = getUpdates()

    message_id = updates[-1]['message']['message_id']
    
    message = updates[-1]['message']
    chat_id = updates[-1]['message']['chat']['id']


    print(f"MESSAGE ID: {message_id}  LAST MESSAGE ID: {last_message_id}")

    if message_id != last_message_id:
        text = message.get('text')
        photo = message.get('photo')

        if text != None:
            if text == "/start":
                
                sendMessage(chat_id, f"<i>welcome to bot!</i>",parse_mode="HTML")
            else:   
                sendMessage(chat_id, f"<i>{text}</i>",parse_mode="HTML")
        elif photo != None:
            file_id = photo[0]['file_id']
            sendPhoto(chat_id, file_id)
        else:
            sendMessage(chat_id, f"other format")

        last_message_id = message_id

    sleep(2)