import numpy as np

def MSE(now , prev ): # mean square error
    diff = now.astype(np.int) - prev.astype(np.int)
    return np.mean(np.square(diff))

def MAE(now , prev): # mean absolute error
    diff = now.astype(np.int) - prev.astype(np.int)
    return np.mean(np.abs(diff))
