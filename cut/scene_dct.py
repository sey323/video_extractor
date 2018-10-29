import cv2
import numpy as np


INTERVAL= 1      # 待ち時間

class MovieIter(object): #動画のフレームを返すイテレータ
    def __init__(self, moviefile, size=None, inter_method=cv2.INTER_AREA):
        #TODO: check if moviefile exists
        self.org = cv2.VideoCapture(moviefile)
        self.framecnt = 0
        self.size = size #frame size
        self.inter_method = inter_method
    def __iter__(self):
        return self
    def __next__(self):
        self.end_flg, self.frame = self.org.read()
        if not self.end_flg: # end of the movie
            raise StopIteration()
        self.framecnt+=1
        if self.size: # resize when size is specified
            self.frame = cv2.resize(self.frame, self.size, interpolation=self.inter_method)
        return self.frame
    def __del__(self): # anyway it works without destructor
        self.org.release()

def MSE(pic): # mean square error
    return np.mean(np.square(pic))

def MAE(pic): # mean absolute error
    return np.mean(np.abs(pic))
