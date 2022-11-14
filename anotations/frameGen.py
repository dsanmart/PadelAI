import cv2
import csv
import os

import shutil
try:
	videoName = "anotations/padel.mp4"
	outputPath = "./VideoPrueba"
	if (not videoName) or (not outputPath):
		raise ''
except:
	print('usage: python3 Frame_Generator.py <videoPath> <outputFolder>')
	exit(1)
if outputPath[-1] != '/':
	outputPath += '/'
	
if os.path.exists(outputPath):
	shutil.rmtree(outputPath)
os.makedirs(outputPath)
#Segment the video into frames
cap = cv2.VideoCapture(videoName)
success, count = True, 0
success, image = cap.read()
while success:
	cv2.imwrite(outputPath + '%04d.png' %(count), image) # 04 para que se guarden numeros de 4 digitos y no perder el orden
	count += 1
	success, image = cap.read()