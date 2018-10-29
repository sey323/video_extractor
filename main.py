import os,sys

import cv2
import numpy as np

sys.path.append('./cut')
from scene_dct import MovieIter,MAE

ESC_KEY = 27     # Escキー
THRESH = 55.55679398148148 # threshold

WINNAME = "test"
cv2.namedWindow(WINNAME)

def main(movie_file):
    picsize = (64, 36)

    frame_cnt = 0
    frame_ultima = np.zeros((*picsize[::-1], 3)) # create empty image

    for frame in MovieIter(movie_file, None):
        frame_penult = frame_ultima
        frame_ultima = cv2.resize(frame, picsize, interpolation=cv2.INTER_AREA) #指定サイズに縮小

        cv2.imshow(WINNAME, frame)
        key = cv2.waitKey(1) # quit when esc-key pressed
        if key == ESC_KEY:
            break

        #差分画像作成
        diff = frame_ultima.astype(np.int) - frame_penult.astype(np.int)

        if MAE(diff)>=THRESH: #閾値よりMAEが大きい場合、カットと判定
            print("Cut detected!: frame {}".format(frame_cnt))
            cv2.imwrite( "{}/{}.jpg".format('test',frame_cnt), frame_ultima)

        frame_cnt+=1


if __name__ == "__main__":
    if ( len( sys.argv ) != 2):   # 引数が足りない場合は、その旨を表示
        print('Usage: # python %s filename' % sys.argv[0])
        quit()

    movie_file = sys.argv[1]
    main(movie_file)
