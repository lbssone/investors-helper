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

from src.accounts_contents import accounts_contents  
from src.news import stock_messages

import twstock
import schedule
# import time
# import datetime


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Dl2P8zbyzLT/ArjCFpS1EjEQQrEXEJqPhI2Qn8Q8mmKGwZNPS5pnDVZwwMPOzasdfsNPiGxCymwoNeQSTtx4HooAlKzvMftmHiUEUkbXAb3v1nYSjMGROkM3kNJqmtNA1nqAY5NgjVcXyiZJxUN2cAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d7eb5d59a2c829f6b7bfac6c3dda309b')

user_set = set()
tsmc = twstock.realtime.get('2330')
tsmc_latest_price = float(tsmc['realtime']['latest_trade_price'])

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
    user_set.add(event.source.user_id)
    print(event.source.user_id)
    user_input = event.message.text.lower().translate(str.maketrans('', '', ''.join(remove_list)))
    
    if user_input in hi_list:
        reply = 'Hi ' + user_name
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    elif user_input == '查看帳務資訊':
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents=accounts_contents
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
        
    elif user_input == '到價':
        tsmc = twstock.realtime.get('2330')
        latest_price = tsmc['realtime']['latest_trade_price']
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='【到價通知】\n台積電目前的股價為{}，已達設定價格'.format(latest_price),
                actions=[
                    URIAction(
                        label='前往app調整',
                        uri='https://www.figma.com/proto/jXjP5VcbA4zUflkzxUAf2Q/Wealth-Tracker?node-id=9%3A66&scaling=contain&fbclid=IwAR24RY2zh7adUKS52LmjkczxdlvapAwT8griY5l-JTrruhrGEDuX8ykEU-Y'
                    ),
                    PostbackAction(
                        label='更改通知價格',
                        display_text='更改通知價格',
                        data='更改通知價格'
                    ),
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, confirm_template_message)
    elif user_input == '投資資訊':
        investment_info_message = TextSendMessage(
            text='請選擇欲查看的投資項目',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackAction(
                            label="股票", 
                            text="股票", 
                            data="投資資訊:股票"
                        ), 
                        image_url='https://cdn3.iconfinder.com/data/icons/science-soft/512/report_arrow_chart_business_graph_stock_data-512.png'
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label="基金", 
                            text="基金",
                            data="投資資訊:基金"

                        ), 
                        image_url='https://image.flaticon.com/icons/png/512/1351/1351514.png'
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label="外匯", 
                            text="外匯",
                            data="投資資訊:外匯"

                        ),
                        image_url='https://cdn4.iconfinder.com/data/icons/business-and-office-3-2/65/108-512.png'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, investment_info_message)
        # investment_info_message = TemplateSendMessage(
        #     alt_text='Buttons template',
        #     template=ButtonsTemplate(
        #         text='請選擇欲查看之投資資訊',
        #         actions=[
        #             URIAction(
        #                 label="股票", 
        #                 uri="https://www.cnyes.com/twstock/index.htm"
        #             ),
        #             URIAction(
        #                 label='基金',
        #                 uri="https://fund.cnyes.com/"
        #             ),
        #             URIAction(
        #                 label='外匯',
        #                 uri="https://www.cnyes.com/forex/"
        #             )
        #         ]
        #     )
        # )
        # line_bot_api.reply_message(event.reply_token, investment_info_message)
    elif user_input == '設定':
        Buttons_template = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='設定',
                text='請選擇欲設定項目',
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
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Buttons_template)
    print('content: ' + event.message.text)

@handler.add(PostbackEvent)
def handle_postback(event):
    postback = event.postback.data
    print('postback: '+postback)
    if postback == '到價通知':
        investment_info_message = TextSendMessage(
            text='請選擇欲設定之項目',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackAction(
                            label="股票", 
                            text="股票", 
                            data="到價通知:股票"
                        ), 
                        image_url='https://cdn3.iconfinder.com/data/icons/science-soft/512/report_arrow_chart_business_graph_stock_data-512.png'
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label="基金", 
                            text="基金",
                            data="到價通知:基金"

                        ), 
                        image_url='https://image.flaticon.com/icons/png/512/1351/1351514.png'
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label="外匯", 
                            text="外匯",
                            data="到價通知:外匯"

                        ),
                        image_url='https://cdn4.iconfinder.com/data/icons/business-and-office-3-2/65/108-512.png'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, investment_info_message)
    elif postback[:4] == '投資資訊':
        if postback[5:] == '股票':
            stock_info_message = []
            for i in range(4):
                stock_info_message.append(
                    FlexSendMessage(
                        alt_text='hello',
                        contents=stock_messages[i]
                    )
                )
            line_bot_api.reply_message(event.reply_token, stock_info_message)

def push_price_notification():
    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='【到價通知】\n台積電目前的股價為{}，已達設定價格'.format(tsmc_latest_price),
            actions=[
                URIAction(
                    label='前往app調整',
                    uri='https://www.figma.com/proto/jXjP5VcbA4zUflkzxUAf2Q/Wealth-Tracker?node-id=9%3A66&scaling=contain&fbclid=IwAR24RY2zh7adUKS52LmjkczxdlvapAwT8griY5l-JTrruhrGEDuX8ykEU-Y'
                ),
                PostbackAction(
                    label='更改通知價格',
                    display_text='更改通知價格',
                    data='更改通知價格'
                ),
            ]
        )
    )
    line_bot_api.push_message(to='U86847ce3e861fa7b94de62652217c96d', messages=confirm_template_message)

def push_accounts_contents():
    flex_message = FlexSendMessage(
            alt_text='hello',
            contents=accounts_contents
        )
    line_bot_api.push_message(to='U86847ce3e861fa7b94de62652217c96d', messages=flex_message)

def push_notification():
    global tsmc_latest_price
    # schedule.every().day.at("17:22").do(push_accounts_contents)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(10)
    if tsmc_latest_price < 330:
        push_price_notification()

push_notification()

@app.route("/charts", methods=['GET'])
def show_charts():
    return render_template('charts.html')

@app.route("/chart2", methods=['GET'])
def show_chart2():
    return render_template('chart2.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    print('line-bot running...')    

