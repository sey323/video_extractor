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


def cut_and_detect( FLAGS , cut_dct , detect_ai , img_size = [240,135]):
    '''
    シーン検出と物体検出を行う．
    Parameters
    ----------
    cut_dct : function(now , before)
        現在のフレームと1つ前のフレームを見てカット位置か確認する．
    '''
    picsize = (640, 360)

    frame_cnt = 0
    frame_ultima = np.zeros((*picsize[::-1], 3)) # create empty image

    HTML_dumper = Dumper(save_path="results/{}/".format(FLAGS.save_path),img_size =img_size)

    # 保存するディレクトリが存在するか確認する．
    save_folders = "results/"+ FLAGS.save_path
    if save_folders and not os.path.exists(os.path.join(save_folders,"img")):
        os.makedirs(os.path.join(save_folders,"img"))
        os.makedirs(os.path.join(save_folders,"exel"))
        os.makedirs(os.path.join(save_folders,"param"))

    # 1秒ごとに画像を処理する．
    for frame , time in MovieIter(FLAGS.movie_path, None ):
        frame_penult = frame_ultima
        frame_ultima = cv2.resize(frame, picsize, interpolation=cv2.INTER_AREA) #指定サイズに縮小

        # シーンの検出
        if cut_dct(frame_ultima,frame_penult)>=FLAGS.thres: #閾値よりMAEが大きい場合、カットと判定
            formatted_time = "{:0>2}:{:0>2}".format(int(time/60),time%60)
            print("Cut detected!: time {}".format(formatted_time))
            # 保存先の名前の設定
            save_img_path = "results/{}/img/{}.jpg".format(FLAGS.save_path,frame_cnt)
            save_half_img_path = "results/{}/exel/{}.jpg".format(FLAGS.save_path,frame_cnt)
            save_param_path = "results/{}/param/{}.txt".format(FLAGS.save_path,frame_cnt)
            detect_ai(frame_ultima , tofile_img = save_img_path , tofile_txt=save_param_path)

            # 画像のリサイズ処理
            img = cv2.imread(save_img_path, cv2.IMREAD_COLOR)
            resize = (img_size[0],img_size[1])
            half_img = cv2.resize(frame_ultima, resize, interpolation=cv2.INTER_AREA)
            cv2.imwrite(save_half_img_path, half_img)

            HTML_dumper.add_scene(frame_cnt,formatted_time,save_param_path)

        frame_cnt+=1

    # HTMLに保存
    HTML_dumper.save_html()



def main(FLAGS):
    # YOLOディテクターの検出
    #yolo = YOLO_TF()
    #yolo = YOLO9000()
    yolo = YOLO()
    detect_ai = yolo.detect_from_cvmat

    # 検出関数の定義
    cut_dct = scene_dct.MAE
    cut_and_detect(FLAGS,cut_dct,detect_ai)

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
