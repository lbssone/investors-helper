from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

accounts_contents = {
    'type': 'carousel',
    'contents': [
        # overview
        {
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
                        "text": "您的投資資產總覽",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": today,
                        "size": "xs",
                        "color": "#aaaaaa",
                        "wrap": True
                    },
                    {
                        "type": "separator",
                        "margin": "md"
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
                                        "text": "   ",
                                        "size": "sm",
                                        "color": "#555555",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "現值(NTD)",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "報酬率",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "股票",
                                        "size": "md",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "17,000",
                                        "size": "md",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "+8%",
                                        "size": "sm",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "基金",
                                        "size": "md",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "13,000",
                                        "size": "md",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "+2.54%",
                                        "size": "sm",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "外匯",
                                        "size": "md",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "5,000",
                                        "size": "md",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-2.03%",
                                        "size": "sm",
                                        "color": "#00b01b",
                                        "align": "end"
                                    }
                                ]
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
                                        "spacing": "sm",
                                        "margin": "xxl",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "總現值",
                                                "weight": "bold",
                                                "size": "md",
                                                "color": "#215c80",
                                                "margin": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "NTD 35,000",
                                                "weight": "bold",
                                                "size": "md",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "spacing": "sm",
                                        "margin": "xxl",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "總報酬率",
                                                "weight": "bold",
                                                "size": "md",
                                                "color": "#215c80",
                                                "margin": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "+5%",
                                                "weight": "bold",
                                                "size": "md",
                                                "color": "#eb0505",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl",
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "margin": "xxl",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "margin": "md",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "  ",
                                                        "size": "md",
                                                        "color": "#555555",
                                                        "weight": "bold",
                                                        "flex": 0
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "投入成本(NTD)",
                                                        "size": "sm",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "margin": "md",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "定存",
                                                        "size": "md",
                                                        "color": "#555555",
                                                        "weight": "bold",
                                                        "flex": 0
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "100,000",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "margin": "md",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "保險",
                                                        "size": "md",
                                                        "color": "#555555",
                                                        "weight": "bold",
                                                        "flex": 0
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "30,000",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "spacing": "sm",
                                                "margin": "xxl",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "總投入成本",
                                                        "weight": "bold",
                                                        "size": "md",
                                                        "color": "#215c80",
                                                        "margin": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "NTD 130,000",
                                                        "weight": "bold",
                                                        "size": "md",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
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
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "查看圖表",
                            "uri": "https://fintech-salon-wealth-tracker.herokuapp.com/charts"
                        }
                    }
                ]
            }
        },
        # stock
        {
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
                        "text": "【股票】資產總覽",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": today,
                        "size": "xs",
                        "color": "#aaaaaa",
                        "wrap": True
                    },
                    {
                        "type": "separator",
                        "margin": "md"
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
                                        "text": "投資標的",
                                        "size": "md",
                                        "weight": "bold",
                                        "color": "#215c80",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "現值(NTD)",
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "報酬率",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "鴻海",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "9,932",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-0.25%",
                                        "size": "sm",
                                        "color": "#00b01b",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "台泥",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "3,021",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "0.00%",
                                        "size": "sm",
                                        "color": "#8f8f8f",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "元大台灣50",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "4,047",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "+0.27%",
                                        "size": "sm",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl",
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "margin": "xxl",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "總現值",
                                        "weight": "bold",
                                        "size": "md",
                                        "color": "#215c80",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "NTD 17,000",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "margin": "xxl",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "總報酬率",
                                        "weight": "bold",
                                        "size": "md",
                                        "color": "#215c80",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "+5%",
                                        "weight": "bold",
                                        "size": "md",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
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
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "詳細資訊",
                            "uri": "https://www.figma.com/proto/jXjP5VcbA4zUflkzxUAf2Q/Wealth-Tracker?node-id=2%3A197&scaling=contain&fbclid=IwAR2Ei6t1lb639XrxtKQ_Xp8_vjOjSaWJAhzV_OJtPQ5DzzQ_Ki21GWwPGXo"
                        }
                    }
                ]
            }
        },
        # fund
        {
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
                        "text": "【基金】資產總覽",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md"
                    },
                    # date
                    {
                        "type": "text",
                        "text": today,
                        "size": "xs",
                        "color": "#aaaaaa",
                        "wrap": True
                    },
                    {
                        "type": "separator",
                        "margin": "md"
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
                                        "text": "  ",
                                        "size": "md",
                                        "weight": "bold",
                                        "color": "#215c80",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "現值(NTD)",
                                        "size": "sm",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "報酬率",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "基富通",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start",
                                        "wrap": True
                                    },
                                    {
                                        "type": "text",
                                        "text": "    ",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "    ",
                                        "size": "sm",
                                        "color": "#00b01b",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "聯博美國收益基金A2(美元)",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start",
                                        "wrap": True
                                    },
                                    {
                                        "type": "text",
                                        "text": "4,000",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "-0.25%",
                                        "size": "sm",
                                        "color": "#00b01b",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "聯博全球高收益債券基金A2(美元)",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "3,021",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "0.00%",
                                        "size": "sm",
                                        "color": "#8f8f8f",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "xl",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "元大",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "   ",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "    ",
                                        "size": "sm",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "元大新中國基金(人民幣)",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "3,085",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "0.00%",
                                        "size": "sm",
                                        "color": "#8f8f8f",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl",
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "xl",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "台新",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "   ",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "    ",
                                        "size": "sm",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "台新中國通基金(新台幣)",
                                        "size": "sm",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "2,894",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "0.00%",
                                        "size": "sm",
                                        "color": "#8f8f8f",
                                        "align": "end"
                                    }
                                ]
                            },
                        ]
                    }
                    # 參考損益
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "台幣參考損益",
                                "weight": "bold",
                                "size": "md",
                                "color": "#215c80",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "含息",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "+98(+1.63%)",
                                        "size": "sm",
                                        "weight": "bold",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "不含息",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "+62(+1.03%)",
                                        "size": "sm",
                                        "weight": "bold",
                                        "color": "#eb0505",
                                        "align": "end"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    # 投入成本
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "投入成本",
                                "weight": "bold",
                                "size": "md",
                                "color": "#215c80",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "NTD",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "12,938",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    # 帳面市值
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "帳面市值",
                                "weight": "bold",
                                "size": "md",
                                "color": "#215c80",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "NTD",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "13,000",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xl"
                    },
                    # 累積總配息
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "paddingBottom": "xl",
                        "contents": [
                            {
                                "type": "text",
                                "text": "累積總配息",
                                "weight": "bold",
                                "size": "md",
                                "color": "#215c80",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "NTD",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "36",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ]
                            }
                        ]
                    },
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "postback",
                            "label": "詳細資訊",
                            "text": "詳細資訊",
                            "data": "詳細資訊:基金"
                        }
                    }
                ]
            }
        },
        # foreign exchange
        {
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
                        "text": "【外匯】資產總覽",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": today,
                        "size": "xs",
                        "color": "#aaaaaa",
                        "wrap": True
                    },
                    {
                        "type": "separator",
                        "margin": "md"
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
                                    "text": "   ",
                                    "size": "sm",
                                    "color": "#555555",
                                    "align": "start"
                                },
                                {
                                    "type": "text",
                                    "text": "持有金額",
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "center"
                                },
                                {
                                    "type": "text",
                                    "text": "損益參考",
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "日幣",
                                            "size": "md",
                                            "color": "#555555",
                                            "weight": "bold",
                                            "align": "start"
                                        },
                        
                                        {
                                            "type": "text",
                                            "text": "￥83,356",
                                            "size": "md",
                                            "color": "#111111",
                                            "weight": "bold",
                                            "align": "center"
                                        },
                                        {
                                            "type": "text",
                                            "text": "+1.63%",
                                            "size": "sm",
                                            "color": "#eb0505",
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
                                                "text": "(NTD 22,865)",
                                                "size": "xxs",
                                                "color": "#111111",
                                                "align": "center"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "美金",
                                            "size": "md",
                                            "color": "#555555",
                                            "weight": "bold",
                                            "align": "start"
                                        },
                        
                                        {
                                            "type": "text",
                                            "text": "$144",
                                            "size": "md",
                                            "color": "#111111",
                                            "weight": "bold",
                                            "align": "center"
                                        },
                                        {
                                            "type": "text",
                                            "text": "+1.99%",
                                            "size": "sm",
                                            "color": "#eb0505",
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
                                                "text": "(NTD 4,339)",
                                                "size": "xxs",
                                                "color": "#111111",
                                                "align": "center"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "歐元",
                                            "size": "md",
                                            "color": "#555555",
                                            "weight": "bold",
                                            "align": "start"
                                        },
                                        {
                                            "type": "text",
                                            "text": "€344",
                                            "size": "md",
                                            "color": "#111111",
                                            "weight": "bold",
                                            "align": "center"
                                        },
                                        {
                                            "type": "text",
                                            "text": "-1.03%",
                                            "size": "sm",
                                            "color": "#00b01b",
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
                                                "text": "(NTD 11,472)",
                                                "size": "xxs",
                                                "color": "#111111",
                                                "align": "center"
                                            }
                                        ]
                                    }
                                ]
                            },
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
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "postback",
                            "label": "詳細資訊",
                            "text": "詳細資訊",
                            "data": "詳細資訊:外匯"
                        }
                    }
                ]
            }
        },
        # other
        {
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
                    "text": "【其他】資產總覽",
                    "weight": "bold",
                    "size": "xl",
                    "margin": "md"
                },
                {
                    "type": "text",
                    "text": "today",
                    "size": "xs",
                    "color": "#aaaaaa",
                    "wrap": True
                },
                {
                    "type": "separator",
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xxl",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "定存",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "md",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "(台新銀行)",
                                "size": "sm",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "金額",
                                "size": "sm",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "到期日",
                                "size": "sm",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "三年期",
                                "size": "sm",
                                "color": "#555555",
                                "weight": "bold",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "80,000",
                                "size": "sm",
                                "color": "#111111",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "2020.12.31",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "一年期",
                                "size": "sm",
                                "color": "#555555",
                                "weight": "bold",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "20,000",
                                "size": "sm",
                                "color": "#111111",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "2020.12.31",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "總計",
                                "size": "sm",
                                "weight": "bold",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "100,000",
                                "size": "sm",
                                "color": "#555555",
                                "weight": "bold",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "         ",
                                "size": "sm",
                                "color": "#111111",
                                "weight": "bold",
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
                        "type": "text",
                        "text": "保險",
                        "weight": "bold",
                        "size": "lg",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "md",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "(新光人壽)",
                                "size": "sm",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "金額",
                                "size": "sm",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "到期日",
                                "size": "sm",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "五動鑫富",
                                "size": "sm",
                                "color": "#555555",
                                "weight": "bold",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "30,000",
                                "size": "sm",
                                "color": "#111111",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "2025.12.31",
                                "size": "sm",
                                "color": "#555555",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "md",
                            "contents": [
                            {
                                "type": "text",
                                "text": "總計",
                                "size": "sm",
                                "weight": "bold",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "30,000",
                                "size": "sm",
                                "color": "#555555",
                                "weight": "bold",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "  ",
                                "size": "sm",
                                "color": "#111111",
                                "weight": "bold",
                                "align": "end"
                            }
                            ]
                        }
                        ]
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
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "postback",
                            "label": "詳細資訊",
                            "text": "詳細資訊",
                            "data": "詳細資訊:其他"
                        }
                    }
                ]
            }
        }
    ]
}