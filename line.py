import random
import string
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Dl2P8zbyzLT/ArjCFpS1EjEQQrEXEJqPhI2Qn8Q8mmKGwZNPS5pnDVZwwMPOzasdfsNPiGxCymwoNeQSTtx4HooAlKzvMftmHiUEUkbXAb3v1nYSjMGROkM3kNJqmtNA1nqAY5NgjVcXyiZJxUN2cAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d7eb5d59a2c829f6b7bfac6c3dda309b')

@app.route('/')
def index():
    return "<p>Hello World!</p>"

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    hi_list = ['hi', 'hello', '嗨', '你好', '哈囉', '你好嗎', '您好', '嘿', '嗨你好']
    bye_list = ['掰掰', '掰', '拜', '拜拜', '再見', '再會', '掰餔', 'bye', 'bye bye', 'good bye']
    friendly_list = ['你好友善', '妳好友善', '你真友善', '妳真友善', '你人真好', '妳人真好']
    curse_words = ['幹你娘', '馬的', '$#@%$%#$%', '靠北', 'shit!', '幹', '閉嘴', '吵死了', '加油好嗎', '我愛你', '你愛我嗎', '寶貝', '汪汪汪', 'I love you', '你在幹嘛']
    remove_list = [' ', '~']
    urls = ['https://imgur.dcard.tw/bPYuNQm.jpg',
        'https://agirls.aotter.net/media/9f0b48ba-f534-44c4-a109-07380d4e07dd.PNG',
        'https://s2.imgs.cc/img/9KR8UQf.jpg', 'https://pbs.twimg.com/media/DJ5KCtiUQAE6juW.jpg', 
        'https://images.plurk.com/1aDwxN9ei4g201BFznRa.jpg']
    
    user_input = event.message.text.lower()
    user_input = user_input.translate(str.maketrans('', '', ''.join(remove_list)))
    if user_input in hi_list:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="你好~~歡迎問我任何問題！"))
    elif user_input in bye_list:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="再會~~有緣再相會"))
    elif user_input in friendly_list:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="謝謝，你人真好！"))
    elif user_input[0] == '喵' and user_input.count(user_input[0]) == len(user_input):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="喵的"))
    elif user_input[0] == '汪' and user_input.count(user_input[0]) == len(user_input):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="喵"))
    elif user_input == '幹' or user_input == '乾' or user_input == '幹你娘' or user_input == '操' or user_input == '干':
        url_index = random.randint(0, len(urls) - 1)
        url = urls[url_index]
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=url, preview_image_url=url))
    elif user_input == '謝謝':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="不客氣~~"))
    else:
        i = random.randint(0, len(curse_words) - 1)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=curse_words[i]))
    user_id = event.source.user_id
    user_set.add(user_id)
    print(user_set)
    print('content: ' + event.message.text)
    


#貼圖處理
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    print("package_id:", event.message.package_id)
    print("sticker_id:", event.message.sticker_id)
     # ref. https://developers.line.me/media/messaging-api/sticker_list.pdf
    sticker_ids = [
        52002734, 52002735, 52002736, 52002737, 52002738, 52002739, 52002740, 52002741, 52002742, 52002743,
        52002744, 52002745, 52002746, 52002747, 52002748, 52002749, 52002750, 52002751, 52002752, 52002753,
        52002754, 52002755, 52002756, 52002757, 52002758, 52002759, 52002760, 52002761, 52002762, 52002763,
        52002764, 52002765, 52002766, 52002767, 52002768, 52002769, 52002770, 5200277, 52002778, 52002779
    ]

    # package_ids = [11537]
    # package_index = random.randint(0, len(package_ids) - 1)
    sticker_index = random.randint(0, len(sticker_ids) - 1)
    # package_id = str(package_ids[package_index])
    sticker_id = str(sticker_ids[sticker_index])
    sticker_message = StickerSendMessage( package_id='11537', sticker_id=sticker_id)
    line_bot_api.reply_message(event.reply_token,sticker_message)


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    url = 'https://i2-prod.bristolpost.co.uk/incoming/article1823830.ece/ALTERNATES/s615/1_The-Feline-World-Gathers-For-The-Supreme-Cat-Show-2017.jpg'
    # url = 'https://agirls.aotter.net/media/9f0b48ba-f534-44c4-a109-07380d4e07dd.PNG'
    line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=url, preview_image_url=url))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
