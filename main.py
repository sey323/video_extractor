import os,sys
import cv2
import numpy as np
import tensorflow as tf

sys.path.append('./opt')
from movie import MovieIter

sys.path.append('./cut')
import scene_dct

sys.path.append('./venders/yolo_tensor')
from YOLO_small_tf import YOLO_TF


def cut_and_detect( FLAGS , cut_dct , detect_ai):
    picsize = (640, 360)

    frame_cnt = 0
    frame_ultima = np.zeros((*picsize[::-1], 3)) # create empty image

    # 保存するディレクトリが存在するか確認する．
    save_folders = "results/"+ FLAGS.save_path
    if save_folders and not os.path.exists(os.path.join(save_folders,"img")):
        os.makedirs(os.path.join(save_folders,"img"))
        os.makedirs(os.path.join(save_folders,"param"))

    # 1秒ごとに画像を処理する．
    for frame in MovieIter(FLAGS.movie_file, None , interval = FLAGS.interval):
        frame_penult = frame_ultima
        frame_ultima = cv2.resize(frame, picsize, interpolation=cv2.INTER_AREA) #指定サイズに縮小

        '''
        cv2.imshow(WINNAME, frame)
        key = cv2.waitKey(1) # quit when esc-key pressed
        if key == ESC_KEY:
            break
        '''

        # シーンの検出
        if cut_dct(frame_ultima,frame_penult)>=FLAGS.thres: #閾値よりMAEが大きい場合、カットと判定
            print("Cut detected!: frame {}".format(frame_cnt))
            save_img_path = "results/{}/img/{}.jpg".format(FLAGS.save_path,frame_cnt)
            save_param_path = "results/{}/param/{}.txt".format(FLAGS.save_path,frame_cnt)
            detect_ai(img = frame_ultima , tofile_img = save_img_path , tofile_txt=save_param_path)

        frame_cnt+=1


def main(FLAGS):
    # YOLOディテクターの検出
    yolo = YOLO_TF('venders/yolo_tensor/weights/YOLO_small.ckpt')
    detect_ai = yolo.detect_from_cvmat

    # 検出関数の定義
    cut_dct = scene_dct.MAE
    cut_and_detect(FLAGS,cut_dct,detect_ai)

if __name__ == "__main__":
    flags = tf.app.flags
    FLAGS = flags.FLAGS

    # 実行するGANモデルの指定．
    flags.DEFINE_string('movie_file', '', '変換する画像.')
    flags.DEFINE_string('save_path', 'test', '生成した画像を保存するディレクトリ．')

    flags.DEFINE_float('thres', 55.55679398148148, '閾値．')
    flags.DEFINE_float('interval', 1.0, '画像を切り抜く最小単位．')

    main(FLAGS)
