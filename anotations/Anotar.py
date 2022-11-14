import cv2
from matplotlib import path as mplPath


class Anotar:
    def __init__(self, image, dest):
        self.image = image
        self.dest = dest

        self.init_params()

    
    def set_image(self, image):
        self.image = image

    
    def can_draw(self, x, y): 
        if any(self.image.labels[i]["polygon"].contains_point((x,y)) for i in self.image.labels): return False
        return True


    def point(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN and self.can_draw(x, y): 
            self.coords = (x,y)
            cv2.circle(self.image.frame, (x,y), 5, (0,255,0), -1)


        elif event == cv2.EVENT_LBUTTONDOWN: self.image.x, self.image.y = x, y

    def visibility(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN and self.can_draw(x, y):
            key = cv2.waitKey(0)
            v = key - 48
            self.visible = v
            text = "V: " + str(v)
            cv2.putText(self.image.frame, text, (x, y), 0, 0.5, (255,255,255))

        elif event == cv2.EVENT_LBUTTONDOWN: self.image.x, self.image.y = x, y

    #0 -> flying
    #1 -> hitting
    #2 -> bouncing
    #3 -> wall
    #4 -> verja (laterales) - This is used to measure serves
    def trayectory_pattern(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN and self.can_draw(x, y):
            key = cv2.waitKey(0)
            t_p = key - 48
            self.trayectory_type = t_p
            text = "TP: " + str(t_p)
            cv2.putText(self.image.frame, text, (x, y), 0, 0.5, (255,255,255))

        elif event == cv2.EVENT_LBUTTONDOWN: self.image.x, self.image.y = x, y

    #0 -> not wall
    #1 -> front wall
    #2 -> right wall
    #3 -> left wall
    #4 -> back wall
    def wall(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN and self.can_draw(x, y):
            key = cv2.waitKey(0)
            w = key - 48
            self.wall_type = w
            text = "W: " + str(w)
            cv2.putText(self.image.frame, text, (x, y), 0, 0.5, (255,255,255))

        elif event == cv2.EVENT_LBUTTONDOWN: self.image.x, self.image.y = x, y


    def save(self):
        with open(self.dest, 'a') as file:
            content = str(self.image.frame_number) + "," + str(self.visible) + "," + str(self.coords[0]) + "," + str(self.coords[1]) + "," + str(self.trayectory_type) + "," + str(self.wall_type) + "\n"
            file.write(content)
        print(content)


    def init_params(self): 
        self.coords = (0,0)
        self.visible = 0
        self.trayectory_type = 0
        self.wall_type = 0

