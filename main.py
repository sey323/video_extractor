import os,sys
import cv2
import numpy as np
import tensorflow as tf

sys.path.append('./opt')
from movie import MovieIter
from dump import Dumper

sys.path.append('./cut')
import scene_dct

sys.path.append('./models/YOLO_small')
from YOLO_small_tf import YOLO_TF
sys.path.append('./models/yolo9000')
from YOLO9000 import YOLO9000
sys.path.append('./models/YOLOv3')
from yolo import YOLO

import module

def main(FLAGS):
    # YOLOディテクターの検出
    #yolo = YOLO_TF()
    #yolo = YOLO9000()
    yolo = YOLO()
    detect_ai = yolo.detect_from_cvmat

    # 検出関数の定義
    cut_dct = scene_dct.MAE
    module.cut_and_detect(FLAGS.movie_path,cut_dct,detect_ai,FLAGS.save_path,FLAGS.thres)

if __name__ == "__main__":
    flags = tf.app.flags
    FLAGS = flags.FLAGS

    # 実行するGANモデルの指定．
    flags.DEFINE_string('movie_path', '', '変換する画像.')
    flags.DEFINE_string('save_path', 'test', '生成した画像を保存するディレクトリ．')

    flags.DEFINE_float('thres', 55.55679398148148, '閾値．')
    '''
    thres
    ------------
    祭り動画:55
    料理動画:15
    '''

    main(FLAGS)
