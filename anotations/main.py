import cv2
from matplotlib import path as mplPath
import argparse

from Imagen import Imagen
from Anotar import Anotar

frame_src= "./padel.mp4"

# parser for running the program
parser = argparse.ArgumentParser(description='Create annotations following the tracknet format.')
parser.add_argument("frame_src", help="Direction to file",default="wall structure.png")
parser.add_argument("outfile", help="Optional output CSV file. Default to annotations.csv",  nargs='?', default='annotations.csv')
parser.add_argument("frame_number", help="Number of the annotated frame. Default to 0", nargs="?", default=1)
args = parser.parse_args()


params_labels = ["VIS", "POINT", "T.PATT", "WALL", "NEW", "SAVE"]
image = Imagen(args.frame_src, 1200, 700, params_labels, args.frame_number)

anotar = Anotar(image, args.outfile)

cv2.namedWindow(args.frame_src)
cv2.setMouseCallback(args.frame_src, anotar.point)
image.labels["POINT"]["name"] = "POINT*"


while True: 
    
    key = cv2.waitKey(1)
    if key == ord("q"): 
        break

    if image.labels["VIS"]["polygon"].contains_point((image.x, image.y)): 
        image.init_labels(image.params_labels)
        image.labels["VIS"]["name"] = "VIS*"
        cv2.setMouseCallback(args.frame_src, anotar.visibility)

    elif image.labels["T.PATT"]["polygon"].contains_point((image.x, image.y)): 
        image.init_labels(image.params_labels)
        image.labels["T.PATT"]["name"] = "T.PATT*"
        cv2.setMouseCallback(args.frame_src, anotar.trayectory_pattern)

    elif image.labels["POINT"]["polygon"].contains_point((image.x, image.y)): 
        image.init_labels(image.params_labels)
        image.labels["POINT"]["name"] = "POINT*"
        cv2.setMouseCallback(args.frame_src, anotar.point)

    elif image.labels["WALL"]["polygon"].contains_point((image.x, image.y)): 
        image.init_labels(image.params_labels)
        image.labels["WALL"]["name"] = "WALL*"
        cv2.setMouseCallback(args.frame_src, anotar.wall)

    elif image.labels["NEW"]["polygon"].contains_point((image.x, image.y)): 
        image.set_frame(args.frame_src)
        image.init_labels(params_labels)
        anotar.set_image(image)

        anotar.init_params()

    elif image.labels["SAVE"]["polygon"].contains_point((image.x, image.y)): 
        anotar.save()
        image.x = -1
        image.y = -1

    image.draw_labels()
    cv2.imshow(args.frame_src, image.frame)

cv2.destroyAllWindows()