import numpy as np
import cv2

def MSE(now , prev ): # mean square error
    diff = now.astype(np.int) - prev.astype(np.int)
    return np.mean(np.square(diff))

def MAE(now , prev): # mean absolute error
    diff = now.astype(np.int) - prev.astype(np.int)
    return np.mean(np.abs(diff))

def MAE_HSV(now , prev): # mean absolute error
    now_ = np.array(now,dtype=np.uint8)
    prev_ = np.array(prev,dtype=np.uint8)
    now_hsv = cv2.cvtColor(now_, cv2.COLOR_BGR2HSV)
    prev_hsv = cv2.cvtColor(prev_, cv2.COLOR_BGR2HSV)
    diff = now_hsv[:,:,(0,1)].astype(np.int) - prev_hsv[:,:,(0,1)].astype(np.int)
    return np.mean(np.abs(diff))

def MAE_block(now , prev ,picsize = (16,9)): # mean absolute error
    now_r = cv2.resize(now, picsize, interpolation=cv2.INTER_AREA) #指定サイズに縮小
    prev_r = cv2.resize(prev, picsize, interpolation=cv2.INTER_AREA) #指定サイズに縮小
    print(prev_r.shape)
    diff = now_r.astype(np.int) - prev_r.astype(np.int)

    return np.mean(np.abs(diff))
