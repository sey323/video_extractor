import sys
from flask import Flask, request,jsonify, abort, make_response

api = Flask(__name__)

# 自作関数の読み込み
sys.path.append('./src/opt')
from movie import MovieIter
from dump import Dumper

sys.path.append('./src/cut')
import scene_dct

sys.path.append('./models/YOLOv3')
from yolo import YOLO

sys.path.append('./src')
import module

# 動画分析API
@api.route('/', methods=['GET'])
def get_movie_analy():
    params = request.args

    if 'movie_path' in params:
        movie_path = params.get('movie_path')
    else:
        return make_response('Please set movie path')

    save_path = 'test'
    if 'save_path' in params:
        save_path =  params.get('save_path')

    thres = 50
    if 'thres' in params:
        thres =  params.get('thres')

    module.cut_and_detect(movie_path,cut_dct,detect_ai,save_path=save_path,thres=int(thres))

    return make_response(save_path)

# エラーハンドリング
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    # 物体認識モデルの定義
    yolo = YOLO()
    detect_ai = yolo.detect_from_cvmat
    cut_dct = scene_dct.MAE
    api.run(host='0.0.0.0', port=3000)
