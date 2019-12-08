import random
import string
import json
from flask import Flask, request, abort, render_template
import os

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
        reply = 'Hi ' + user_name
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    if user_input == '查看帳務資訊':
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents={
                "type": "bubble",
                "styles": {
                    "footer": {
                        "separator": True
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "RECEIPT",
                            "weight": "bold",
                            "color": "#1DB446",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": "您的投資資產總覽",
                            "weight": "bold",
                            "size": "xxl",
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                            "size": "xs",
                            "color": "#aaaaaa",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "xxl",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Energy Drink",
                                            "size": "sm",
                                            "color": "#555555",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$2.99",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Chewing Gum",
                                            "size": "sm",
                                            "color": "#555555",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$0.99",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Bottled Water",
                                            "size": "sm",
                                            "color": "#555555",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$3.33",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "separator",
                                    "margin": "xxl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "margin": "xxl",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "ITEMS",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "3",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "TOTAL",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$7.31",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "CASH",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$8.0",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "CHANGE",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$0.69",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "PAYMENT ID",
                                    "size": "xs",
                                    "color": "#aaaaaa",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "#743289384279",
                                    "color": "#aaaaaa",
                                    "size": "xs",
                                    "align": "end"
                                }
                            ]
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#f2aa5c",
                            "action": {
                                "type": "uri",
                                "label": "查看圖表",
                                "uri": "https://investors-helper.herokuapp.com/charts"
                            }
                        },
                        {
                            "type": "button",
                            "style": "secondary",
                            "action": {
                                "type": "postback",
                                "label": "投資帳務列表",
                                "text": "投資帳務列表",
                                "data": "投資帳務列表"
                            }
                        }
                    ]
                }
            }
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
        
    elif user_input == 'no':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='no'))
    elif user_input == '投資資訊':
        investment_info_message = TextSendMessage(
            text='請選擇欲查看之資訊',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="股票", text="股票"), image_url='https://cdn3.iconfinder.com/data/icons/science-soft/512/report_arrow_chart_business_graph_stock_data-512.png'),
                    QuickReplyButton(action=MessageAction(label="基金", text="基金"), image_url='https://image.flaticon.com/icons/png/512/1351/1351514.png'),
                    QuickReplyButton(action=MessageAction(label="外匯", text="外匯"), image_url='https://cdn4.iconfinder.com/data/icons/business-and-office-3-2/65/108-512.png')
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, investment_info_message)
    elif user_input == 'confirm':
        Confirm_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text='這就是ConfirmTemplate,用於兩種按鈕選擇',
                actions=[                              
                    PostbackTemplateAction(
                        label='Yes',
                        text='Yes',
                        data='yes'
                    ),
                    MessageTemplateAction(
                        label='No',
                        text='No'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Confirm_template)
    elif user_input == '設定':
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/close-up-of-cat-wearing-sunglasses-while-sitting-royalty-free-image-1571755145.jpg',
                        title='this is menu1',
                        text='description1',
                        actions=[
                            PostbackTemplateAction(
                                label='資產變動提醒',
                                text='資產變動提醒',
                                data='資產變動提醒'
                            ),
                            PostbackTemplateAction(
                                label='到價通知',
                                text='到價通知',
                                data='到價通知'
                            ),
                            PostbackTemplateAction(
                                label='到期日通知',
                                text='到期日通知',
                                data='到期日通知'
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
                        thumbnail_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/close-up-of-cat-wearing-sunglasses-while-sitting-royalty-free-image-1571755145.jpg',
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
    print('content: ' + event.message.text)

@handler.add(PostbackEvent)
def handle_postback(event):
    postback = event.postback.data
    if postback == '股票:帳務' or postback == '基金:帳務' or postback == '外匯:帳務' or postback == '定存:帳務':
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents={
                "type": "bubble",
                "styles": {
                    "footer": {
                        "separator": True
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "RECEIPT",
                            "weight": "bold",
                            "color": "#1DB446",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": "您的{}資產總覽".format(postback[:2]),
                            "weight": "bold",
                            "size": "xxl",
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                            "size": "xs",
                            "color": "#aaaaaa",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "xxl",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Energy Drink",
                                            "size": "sm",
                                            "color": "#555555",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$2.99",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Chewing Gum",
                                            "size": "sm",
                                            "color": "#555555",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$0.99",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Bottled Water",
                                            "size": "sm",
                                            "color": "#555555",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$3.33",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "separator",
                                    "margin": "xxl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "margin": "xxl",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "ITEMS",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "3",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "TOTAL",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$7.31",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "CASH",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$8.0",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "CHANGE",
                                            "size": "sm",
                                            "color": "#555555"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$0.69",
                                            "size": "sm",
                                            "color": "#111111",
                                            "align": "end"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "PAYMENT ID",
                                    "size": "xs",
                                    "color": "#aaaaaa",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "#743289384279",
                                    "color": "#aaaaaa",
                                    "size": "xs",
                                    "align": "end"
                                }
                            ]
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#f2aa5c",
                            "action": {
                                "type": "uri",
                                "label": "查看圖表",
                                "uri": "https://investors-helper.herokuapp.com/charts"
                            }
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif postback == '投資帳務列表':
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://cdn2-www.dogtime.com/assets/uploads/2019/10/DogPopcorn1.jpg',
                title='{}的帳務資訊列表'.format(user_name),
                text='請選擇欲查看之帳務',
                actions=[
                    PostbackAction(
                        label='股票',
                        display_text='股票',
                        data='股票:帳務'
                    ),
                    PostbackAction(
                        label='基金',
                        display_text='基金',
                        data='基金:帳務'
                    ),
                    PostbackAction(
                        label='外匯',
                        display_text='外匯',
                        data='外匯:帳務'
                    ),
                    PostbackAction(
                        label='定存',
                        display_text='定存',
                        data='定存:帳務'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        # bubble = BubbleContainer(
        #     direction='ltr',
        #     hero=ImageComponent(
        #         url='https://cdn2-www.dogtime.com/assets/uploads/2019/10/DogPopcorn1.jpg',
        #         size='full',
        #         aspect_ratio='20:13',
        #         aspect_mode='cover',
        #         action=URIAction(uri='http://example.com', label='label')
        #     ),
        #     body=BoxComponent(
        #         layout='vertical',
        #         contents=[
        #             # title
        #             TextComponent(text='您的{}資產總覽'.format(postback[:2]), weight='bold', size='xl'),
        #             # review
        #             # BoxComponent(
        #             #     layout='baseline',
        #             #     margin='md',
        #             #     contents=[
        #             #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
        #             #         IconComponent(size='sm', url='https://example.com/grey_star.png'),
        #             #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
        #             #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
        #             #         IconComponent(size='sm', url='https://example.com/grey_star.png'),
        #             #         TextComponent(text='4.0', size='sm', color='#999999', margin='md',
        #             #                       flex=0)
        #             #     ]
        #             # ),
        #             # info
        #             BoxComponent(
        #                 layout='vertical',
        #                 margin='lg',
        #                 spacing='sm',
        #                 contents=[
        #                     BoxComponent(
        #                         layout='baseline',
        #                         spacing='sm',
        #                         contents=[
        #                             TextComponent(
        #                                 text='Place',
        #                                 color='#aaaaaa',
        #                                 size='sm',
        #                                 flex=1
        #                             ),
        #                             TextComponent(
        #                                 text='Shinjuku, Tokyo',
        #                                 wrap=True,
        #                                 color='#666666',
        #                                 size='sm',
        #                                 flex=5
        #                             )
        #                         ],
        #                     ),
        #                     BoxComponent(
        #                         layout='baseline',
        #                         spacing='sm',
        #                         contents=[
        #                             TextComponent(
        #                                 text='Time',
        #                                 color='#aaaaaa',
        #                                 size='sm',
        #                                 flex=1
        #                             ),
        #                             TextComponent(
        #                                 text="10:00 - 23:00",
        #                                 wrap=True,
        #                                 color='#666666',
        #                                 size='sm',
        #                                 flex=5,
        #                             ),
        #                         ],
        #                     ),
        #                 ],
        #             )
        #         ],
        #     ),
        #     footer=BoxComponent(
        #         layout='vertical',
        #         spacing='sm',
        #         contents=[
        #             # callAction, separator, websiteAction
        #             SpacerComponent(size='sm'),
        #             # callAction
        #             ButtonComponent(
        #                 style='primary',
        #                 color='#f2aa5c',
        #                 height='sm',
        #                 action=URIAction(label='查看圖表', uri='https://investors-helper.herokuapp.com/charts'),
        #             ),
        #             # separator
        #             SeparatorComponent(),
        #             # websiteAction
        #             ButtonComponent(
        #                 style='link',
        #                 height='sm',
        #                 action=URIAction(label='WEBSITE', uri="https://example.com")
        #             )
        #         ]
        #     ),
        # )
        # message = FlexSendMessage(alt_text="hello", contents=bubble)
        # line_bot_api.reply_message(event.reply_token, message)

@app.route("/charts", methods=['GET'])
def show_charts():
    return render_template('charts.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
