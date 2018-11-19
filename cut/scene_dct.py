import numpy as np
import cv2

def MSE(now , prev ): # mean square error
    diff = now.astype(np.int) - prev.astype(np.int)
    return np.mean(np.square(diff))

def MAE(now , prev): # mean absolute error
    diff = now.astype(np.int) - prev.astype(np.int)
    return np.mean(np.abs(diff))

def MAE_HSV(now , prev): # mean absolute error
    now = cv2.cvtColor(now, cv2.COLOR_BGR2HSV)
    prev = cv2.cvtColor(prev, cv2.COLOR_BGR2HSV)

    diff = now[:,:,:1].astype(np.int) - prevn[:,:,:1].astype(np.int)
    return np.mean(np.abs(diff))
