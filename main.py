import os,sys
import cv2
import numpy as np

sys.path.append('./opt')
from movie import MovieIter

sys.path.append('./cut')
import scene_dct

sys.path.append('./venders/yolo_tensor')
from YOLO_small_tf import YOLO_TF


ESC_KEY = 27     # Escキー
THRESH = 55.55679398148148 # threshold

WINNAME = "test"
cv2.namedWindow(WINNAME)

def cut_and_detect( movie_file , cut_dct , detect_ai):
    picsize = (640, 360)

    frame_cnt = 0
    frame_ultima = np.zeros((*picsize[::-1], 3)) # create empty image

    # 1秒ごとに画像を処理する．
    for frame in MovieIter(movie_file, None , interval = 1):
        frame_penult = frame_ultima
        frame_ultima = cv2.resize(frame, picsize, interpolation=cv2.INTER_AREA) #指定サイズに縮小

        '''
        cv2.imshow(WINNAME, frame)
        key = cv2.waitKey(1) # quit when esc-key pressed
        if key == ESC_KEY:
            break
        '''

        # シーンの検出
        if cut_dct(frame_ultima,frame_penult)>=THRESH: #閾値よりMAEが大きい場合、カットと判定
            print("Cut detected!: frame {}".format(frame_cnt))
            filename = "{}/{}.jpg".format('test',frame_cnt)
            detect_ai(img = frame_ultima , tofile_img = filename , tofile_txt=filename+".txt")

        frame_cnt+=1


def main(movie_file):
    # YOLOディテクターの検出
    yolo = YOLO_TF('venders/yolo_tensor/weights/YOLO_small.ckpt')
    detect_ai = yolo.detect_from_cvmat

    # 検出関数の定義
    cut_dct = scene_dct.MAE
    cut_and_detect(movie_file,cut_dct,detect_ai)


if __name__ == "__main__":
    if ( len( sys.argv ) != 2):   # 引数が足りない場合は、その旨を表示
        print('Usage: # python %s filename' % sys.argv[0])
        quit()

    movie_file = sys.argv[1]
    main(movie_file)
