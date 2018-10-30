import sys
from darkflow.net.build import TFNet
import cv2
import numpy as np

class YOLO9000:
    def __init__(self,weights_file="models/yolo9000/yolo9000.weights",thresulthold = 0.1):
        self.options = {"model":"models/yolo9000/cfg/yolo9000.cfg",
                        "load":weights_file,
                        "thresulthold":thresulthold}

        self.tfnet = TFNet(self.options)
        self.dect_objects = ''

    def detect_from_cvmat( self , img , tofile_img , tofile_txt ):
        imgcv = np.asarray(img)
        result_image = imgcv
        results = self.tfnet.return_predict(img)

        print(results)
        for result in results:
            if not result['confidence']:
                continue
            self.dect_objects += result['label']
            result_image = cv2.rectangle(imgcv, (result['topleft']['x'], result['topleft']['y']), (result['bottomright']['x'], result['bottomright']['y']), (0, 0, 255), 5)
            text = result['label'] + " " + ('%.2f' % result['confidence'])
            cv2.putText(result_image,
                        text,
                        (result['topleft']['x']+10, result['topleft']['y']-5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 255),
                        2)


        with open(tofile_txt, mode='w') as f:
            f.write(self.dect_objects )
        cv2.imwrite( tofile_img, result_image)
