import json

import requests

webhook_url = ""


def send_msg(title, content):
    params = {
        "msg_type": "interactive",
        "card": json.dumps({
            "config": {
                "wide_screen_mode": True
            },
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": title
                }
            },
            "elements": [
                {
                    "tag": "div",
                    "fields": [
                        {
                            "is_short": False,
                            "text": {
                                "tag": "lark_md",
                                "content": content
                            }
                        },

                    ]
                },
            ]
        })

    }

    resp = requests.post(webhook_url, json=params)
    print(resp.text)
