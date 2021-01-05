# coding: utf-8
import os
import sys


sys.path.append(os.pardir)

# botアカウントのトークンを指定
API_TOKEN = "xoxb-45036031109-486285651590-ERRlCaW43c6yqoCxiQtvfyix"

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "みんな話しかけて！"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ["plugins"]
