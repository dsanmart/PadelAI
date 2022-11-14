import cv2
from matplotlib import path as mplPath
import numpy as np

class Imagen:
    def __init__(self, src, preferred_width, preferred_height, params_labels, frame_number):
        img = cv2.imread(src)
        self.height, self.width, _ = img.shape

        self.preferred_width = preferred_width
        self.preferred_height = preferred_height

        self.frame = cv2.resize(img, (preferred_width, preferred_height))
        self.frame_number = frame_number

        self.labels = {}
        self.params_labels = params_labels
        self.x = -1
        self.y = -1

        self.init_labels(params_labels)

    def set_frame(self, src):
        img = cv2.imread(src)
        self.frame = cv2.resize(img, (self.preferred_width, self.preferred_height))


    def get_scale(self): 

        height_coef = self.height/self.preferred_height
        width_coef = self.width/self.preferred_width

        return width_coef, height_coef 


    def get_point(self, event, x, y, flags, params): 

        if event == cv2.EVENT_LBUTTONDOWN:
            self.x, self.y = x, y


    def init_labels(self, params):        
        x, y = 10, 10
        for i in params:

            self.labels[i] = {}
            self.labels[i]["polygon"] = mplPath.Path(np.array([[x, y], [x+120, y], [x+120, y+50], [x, y+50]]))
            self.labels[i]["bbox"] = [(x, y), (x+120, y+50)]
            self.labels[i]["name"] = i
            y += 75

    def draw_labels(self):
        for i in self.labels:
            cv2.rectangle(self.frame, self.labels[i]["bbox"][0], self.labels[i]["bbox"][1], (0,0,255), -1)
            cv2.putText(self.frame, self.labels[i]["name"], (self.labels[i]["bbox"][0][0]+40, self.labels[i]["bbox"][0][1]+25), 0, 0.5, (255,255,255))