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

    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name
    user_input = event.message.text.lower().translate(str.maketrans('', '', ''.join(remove_list)))
    

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
                            # PostbackTemplateAction(
                            #     label='保險',
                            #     text='保險',
                            #     data='保險'
                            # ),
                            # PostbackTemplateAction(
                            #     label='定存',
                            #     text='定存',
                            #     data='定存'
                            # ),
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
    elif user_input == 'flex':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://example.com/cafe.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Brown Cafe', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Shinjuku, Tokyo',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='CALL', uri='tel:000000'),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='WEBSITE', uri="https://example.com")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif user_input == 'confirm':
        message = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Are you sure?",
                    "margin": "md"
                },
                {
                    "type": "spacer"
                }
                ],
                "action": {
                "type": "uri",
                "label": "View detail",
                "uri": "http://linecorp.com/",
                "altUri": {
                    "desktop": "http://example.com/page/123"
                }
                }
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "Yes",
                    "text": "yes"
                    },
                    "height": "sm"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "No",
                    "text": "no"
                    },
                    "height": "sm"
                }
                ],
                "flex": 0
            },
            "styles": {
                "footer": {
                "separator": "true"
                }
            }
        }
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    print('content: ' + event.message.text)

@handler.add(PostbackEvent)
def handle_postback(event):
    postback = event.postback.data
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=postback+'~~~'))



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
