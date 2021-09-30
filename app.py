from flask import Flask, json, jsonify, render_template ,request ,make_response

import geopy.distance as ps
from numpy.lib.function_base import append
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("product").sheet1
data = sheet.get_all_records()
listdata = pd.DataFrame(data)
print(listdata)

app = Flask(__name__)


def create_flex(name , tel , job):
    flex_json = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip4.jpg",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "150:196",
                    "gravity": "center",
                    "flex": 1
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip5.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:98",
                        "gravity": "center"
                    },
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip6.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "150:98",
                        "gravity": "center"
                    }
                    ],
                    "flex": 1
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "NEW",
                        "size": "xs",
                        "color": "#ffffff",
                        "align": "center",
                        "gravity": "center"
                    }
                    ],
                    "backgroundColor": "#EC3D44",
                    "paddingAll": "2px",
                    "paddingStart": "4px",
                    "paddingEnd": "4px",
                    "flex": 0,
                    "position": "absolute",
                    "offsetStart": "18px",
                    "offsetTop": "18px",
                    "cornerRadius": "100px",
                    "width": "48px",
                    "height": "25px"
                }
                ]
            }
            ],
            "paddingAll": "0px"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "contents": [],
                        "size": "xl",
                        "wrap": True,
                        "text": "ชื่อ " + str(name) + " : หน้าที่ " + str(job) ,
                        "color": "#ffffff",
                        "weight": "bold"
                    }
                    ],
                    "spacing": "sm"
                }
                ]
            }
            ],
            "paddingAll": "20px",
            "backgroundColor": "#464F69"
        }
    }
    return flex_json
    #เทสปกติผ่าน api
    #return flex_json

    #สำหรับบอทต้อง return

def formatObject(flex_json):
    return [{
            "type": "flex",
            "altText": "Show Carousel",
            "contents": {
                "type": "carousel",
                "contents": flex_json 
            }
        }]

def flex_all_order(name ):
    jsonData = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "ชื่อ "+ str(name),
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                {
                    "type": "icon",
                    "size": "sm",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                    "type": "icon",
                    "size": "sm",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                    "type": "icon",
                    "size": "sm",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                    "type": "icon",
                    "size": "sm",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                    "type": "icon",
                    "size": "sm",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                },
                {
                    "type": "text",
                    "text": "4.0",
                    "size": "sm",
                    "color": "#999999",
                    "margin": "md",
                    "flex": 0
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Place",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": "test",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
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
                "style": "link",
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "CALL",
                "uri": "https://linecorp.com"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "WEBSITE",
                "uri": "https://linecorp.com"
                }
            },
            {
                "type": "spacer",
                "size": "sm"
            }
            ],
            "flex": 0
        }
    }
    return jsonData

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get_product")
def get_product():
    data = sheet.get_all_records()
    listdata = pd.DataFrame(data)
    print(listdata)

    flex_message = []
    for i in range( len(listdata)):
        item = listdata.iloc[i]
        print(item['ชื่อ'])
        jsonData = flex_all_order(item['ชื่อ'])  
        flex_message.append(jsonData)
    print(flex_message)
    response= make_response(
                jsonify({"line_payload": formatObject(flex_message) }),
                200,
    )
    response.headers["Response-Type"] = "object"
    return response

@app.route("/get_profile")
def get_profile():
    name = "test tanup"
    jsonData = create_flex(name)
    response= make_response(
                jsonify({"line_payload": jsonData}),200,
    )
    response.headers["Response-Type"] = "object"
    return response  #? สำหรับ API แบบที่ 2 

@app.route("/insert_member")
def insert_member():
    name = request.args.get("name")
    tel = request.args.get("tel")
    job = request.args.get("job")
    add_data = [name, int(tel),str(job)]
    data = sheet.get_all_records()
    listdata = pd.DataFrame(data)
    index = int(len(listdata) + 2)
    sheet.insert_row(add_data , index)
    return "ok"

@app.route("/get_order")
def get_order():
    name = request.args.get("name")
    data = sheet.get_all_records()
    listdata = pd.DataFrame(data)
    data = listdata[listdata['ชื่อ'] == name ]
    if len(data) == 0 :
        return "no data"
    jsonData = create_flex(
        data.iloc[0]["ชื่อ"] ,
        data.iloc[0]["เบอร์โทร"] ,
        data.iloc[0]["หน้าที่"] ,
    )
    response= make_response(
                jsonify({"line_payload": formatObject([jsonData]) }),200,
    )
    response.headers["Response-Type"] = "object"
    return response
    
    
    # jsonData = {
    #     "name":data.iloc[0]['ชื่อ'],
    #     "tel":str(data.iloc[0]['เบอร์โทร']),
    #     "order":str(data.iloc[0]['หน้าที่'])
    # }
    # return jsonify(jsonData)

# @app.route("/insert_order")
# def insert_order():
#     name = request.args.get("name")
#     tel = request.args.get("tel")
#     order = request.args.get("order")
#     add_data = [name, str(tel),str(order)]
#     data = sheet.get_all_records()
#     listdata = pd.DataFrame(data)
#     index = int(len(listdata) + 2)
#     sheet.insert_row(add_data , index)
#     return "ok"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
