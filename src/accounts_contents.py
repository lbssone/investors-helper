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
                    # {
                    #     "type": "text",
                    #     "text": "RECEIPT",
                    #     "weight": "bold",
                    #     "color": "#1DB446",
                    #     "size": "sm"
                    # },
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
                        "borderWidth": "normal",
                        "borderColor": "#215c80",
                        "cornerRadius": "md",
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
                                "text": "50,000",
                                "size": "md",
                                "color": "#111111",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "(+0.5%)",
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
                                "text": "30,000",
                                "size": "md",
                                "color": "#111111",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "(+0.5%)",
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
                                "text": "30,000",
                                "size": "md",
                                "color": "#111111",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "(+0.5%)",
                                "size": "sm",
                                "color": "#eb0505",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "總計",
                                "size": "md",
                                "weight": "bold",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "text": "110,000",
                                "size": "md",
                                "color": "#111111",
                                "weight": "bold",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "(+0.5%)",
                                "size": "sm",
                                "color": "#eb0505",
                                "weight": "bold",
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
                            "contents": [
                            {
                                "type": "text",
                                "text": "定存",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "NTD 100,000",
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
                                "text": "保險",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "NTD 30,000",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
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
                            "type": "text",
                            "text": "總現值",
                            "weight": "bold",
                            "size": "lg",
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
                                "size": "md",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "240,000",
                                "size": "md",
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
                                "spacing": "sm",
                                "margin": "xxl",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "總現值",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#215c80",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "NTD 110,000",
                                        "size": "md",
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
                                        "text": "總報酬率",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#215c80",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "+5%",
                                        "size": "md",
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
                                        "text": "   ",
                                        "size": "sm",
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
                                        "size": "md",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "9,932",
                                        "size": "md",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "(-0.25%)",
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
                                        "size": "md",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "4,300",
                                        "size": "md",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "(0.00%)",
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
                                        "size": "md",
                                        "color": "#555555",
                                        "weight": "bold",
                                        "align": "start"
                                    },
                                    {
                                        "type": "text",
                                        "text": "4,300",
                                        "size": "md",
                                        "color": "#111111",
                                        "align": "center"
                                    },
                                    {
                                        "type": "text",
                                        "text": "(-0.27%)",
                                        "size": "sm",
                                        "color": "#eb0505",
                                        "align": "end"
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
                        "style": "primary",
                        "color": "#f2aa5c",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "查看圖表",
                            "uri": "https://fintech-salon-wealth-tracker.herokuapp.com/chart2"
                        }
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "postback",
                            "label": "詳細資訊",
                            "text": "詳細資訊",
                            "data": "詳細資訊:股票"
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
                                        "text": "+28(+0.47%)",
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
                                        "text": "-8(-0.13%)",
                                        "size": "sm",
                                        "weight": "bold",
                                        "color": "#00b01b",
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
                                        "text": "TWD",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "10,000",
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
                                        "text": "TWD",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "10,000",
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
                                        "text": "TWD",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "50",
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
                        "style": "primary",
                        "color": "#f2aa5c",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "查看圖表",
                            "uri": "https://fintech-salon-wealth-tracker.herokuapp.com/chart2"
                        }
                    },
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
                            "type": "text",
                            "text": "外匯活存",
                            "weight": "bold",
                            "size": "md",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "美金",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$10,000",
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
                                "text": "日幣",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "￥30,000",
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
                            "type": "text",
                            "text": "外匯定存",
                            "weight": "bold",
                            "size": "md",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "美金",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$10,000",
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
                                "text": "日幣",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "￥30,000",
                                "size": "sm",
                                "color": "#111111",
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
                        "style": "primary",
                        "color": "#f2aa5c",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "查看圖表",
                            "uri": "https://fintech-salon-wealth-tracker.herokuapp.com/chart2"
                        }
                    },
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
                                "type": "text",
                                "text": "定存",
                                "weight": "bold",
                                "size": "md",
                                "margin": "md"
                            },
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
                                "type": "text",
                                "text": "保險",
                                "weight": "bold",
                                "size": "md",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
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
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "查看圖表",
                            "uri": "https://fintech-salon-wealth-tracker.herokuapp.com/chart2"
                        }
                    },
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