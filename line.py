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
    remove_list = [' ', '~']
    
    user_input = event.message.text.lower()
    user_input = user_input.translate(str.maketrans('', '', ''.join(remove_list)))
    if user_input in hi_list:
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://cdn2-www.dogtime.com/assets/uploads/2019/10/DogPopcorn1.jpg',
                        title='this is menu1',
                        text='description1',
                        actions=[
                            PostbackTemplateAction(
                                label='股票',
                                text='股票',
                                data='股票'
                            ),
                            PostbackTemplateAction(
                                label='基金',
                                text='基金',
                                data='基金'
                            ),
                            PostbackTemplateAction(
                                label='外匯',
                                text='外匯',
                                data='外匯'
                            ),
                            PostbackTemplateAction(
                                label='保險',
                                text='保險',
                                data='保險'
                            ),
                            PostbackTemplateAction(
                                label='定存',
                                text='定存',
                                data='定存'
                            ),
                            # MessageTemplateAction(
                            #     label='message1',
                            #     text='message text1'
                            # ),
                            # URITemplateAction(
                            #     label='uri1',
                            #     uri='http://example.com/1'
                            # )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cdn2-www.dogtime.com/assets/uploads/2019/10/DogPopcorn1.jpg',
                        title='this is menu2',
                        text='description2',
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='連結2',
                                uri='http://example.com/2'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif user_input == 'no':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='no'))
    elif user_input == 'profile':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                    TextSendMessage(text='Display name: ' + profile.display_name),
                #     TextSendMessage(text='Status message: ' + profile.status_message)
                # ]
            )
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Bot can't use profile API without user ID"))
    user_id = event.source.user_id
    print('content: ' + event.message.text)

@handler.add(PostbackEvent)
def handle_postback(event):
    postback = event.postback.data
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=postback+'~~~'))



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
