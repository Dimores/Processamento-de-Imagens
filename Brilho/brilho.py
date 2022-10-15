import cv2
import numpy as np
import os


def main():
	width = 1280
	hieght = 720
	channel = 3

	fps = 10
	sec = 20

	fourcc = cv2.VideoWriter_fourcc(*'MP42')

	video = cv2.VideoWriter('image_to_video.avi', fourcc, float(fps), (width, hieght))

	directry = r'C:\Users\diego\Documents\Atividades\Python\Animacao\imgs'

	current_contrast = 0
	
	t = 0    #Variavel para fade ind
	g = 30   #Variavel para fade out
	
	for frame_count in range(fps*sec):
		
		img = cv2.imread("imgs/dog.jpg")
		img_resize = cv2.resize(img, (width, hieght))

		#Inicia com a cor preta(o de brilho) ate 1 segundo
		if((frame_count >= 1) and (frame_count < 10)):
		   img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = 0) 
		   video.write(img_resize)
		   print(frame_count)
		   
		#Fade in
		if((frame_count > 10) and (frame_count <= 30)):
		   img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t) 
		   video.write(img_resize)
		   t += 13
		   
		#Normal
		if((frame_count > 30) and (frame_count < 80)):
		   video.write(img_resize)
		   
		#Fade out
		if((frame_count > 80) and (frame_count <= 100)):
		   img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = g)
		   video.write(img_resize)
		   t -= 13
		   
if __name__ == "__main__":
	main()
