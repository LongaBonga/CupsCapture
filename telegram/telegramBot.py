import os
import telepot
from PIL import Image

def bot_preparation():
        
    if os.path.exists('./telegram/token.txt') and os.path.getsize('./telegram/token.txt'):
        with open('./telegram/token.txt', "r") as f:
            token = f.read()[:-2]

    else:

        f = open("./telegram/token.txt","w+")
        token = input('input telegram bot token \n')
        f.write('{} \n'.format(token))
        f.close()

    bot = telepot.Bot(token)
    
    print(token)


    if os.path.exists('./telegram/user_id.txt') and os.path.getsize('./telegram/user_id.txt'):
        with open('./telegram/user_id.txt', "r") as f:
            id = f.read()[:-2]
    else:

        f = open("./telegram/user_id.txt","w+")
        input('Write your telegram bot smth and press Etner')

        response = bot.getUpdates()
        id = response[0]['message']['from']['id']
        f.write('{} \n'.format(id))
        f.close()
    return bot, token, id


def send_mes(bot, id, image):

    bot.sendMessage(id, 'put the mugs away!!!')
    img = Image.fromarray(image[...,::-1])
    img.save("./out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    bot.sendPhoto(id, photo=open('./out.jpg', 'rb'))