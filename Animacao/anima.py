import numpy as np
import cv2
import os

width = 1280
hieght = 720
channel = 3

fps = 10
sec = 10

fourcc = cv2.VideoWriter_fourcc(*'MP42')

video = cv2.VideoWriter('image_to_video.avi', fourcc, float(fps), (width, hieght))

directry = r'C:\Users\diego\Documents\Atividades\Python\Animacao\imgs'

before_contrast = 0
current_contrast = 0

before_brightness = 0
current_brightness = 200

contadorContraste = 0
contadorBrilho = 0

for frame_count in range(fps*sec):

    img = cv2.imread("imgs/house.jpg")
    img_resize = cv2.resize(img, (width, hieght))

    if((sec == 0) and (sec <= 3)):
        img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = current_brightness) #Método que aplica uma mudança em toda matriz

    video.write(img_resize)

video.release()
