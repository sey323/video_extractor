# coding: utf-8
import os
import sys

sys.path.append(os.pardir)

from datetime import datetime

from slackbot.bot import respond_to  # @botname: で反応するデコーダ
from slackbot.bot import listen_to  # @botname: で反応するデコーダ

import requests
import slackbot_settings


# 動画読み込みの開始
@respond_to(r"^venom,(.*)")
@listen_to(r"^venom,(.*)")
@respond_to(r"^v,(.*)")
@listen_to(r"^v,(.*)")
def start_client(message, args):
    args = args.replace("<", "").replace(">", "").split(",")

    # 入力から引数を決定
    if len(args) == 1:
        thres = 50
    else:
        thres = args[1]

    movie_path = args[0]
    now = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    save_path = "api/" + now

    message.reply("閾値" + str(thres) + "で実行中")
    response = requests.get(
        "http://video-yolo:3000/",
        params={"movie_path": movie_path, "thres": thres, "save_path": save_path},
    )

    files = {"file": open("results/" + save_path + "/result.xlsx", "rb")}
    param = {"token": slackbot_settings.API_TOKEN, "channels": "video"}
    res = requests.post(
        url="https://slack.com/api/files.upload", params=param, files=files
    )
    message.reply("できたよ")


# ヘルプ
@listen_to(r"^help$")
@respond_to(r"^help$")
@listen_to(r"^h$")
@respond_to(r"^h$")
def helper(message):
    help_message = ">>> \
    使い方 \n\
    ●コマンド\n \
    `v,{yotubeの動画のURL},{閾値}` \n \
    \tyoutubeの動画を閾値で切り抜き \n \
    ●閾値について \n \
    範囲:0.00~100.00 \n\
    閾値が小さい：画面の少しの変化でカットする．\n\
    閾値が大きい：画面の大きな変化でカットする．\n\
    料理動画：15〜25 \n\
    観光動画：50〜60 \n\
    ※検証中なので参考までに"

    message.reply(help_message)