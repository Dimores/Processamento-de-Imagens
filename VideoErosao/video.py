import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

#Função que pega uma imagem e cria um video de erosao
def videoErosao(img):
    #kernel
    kernel = np.ones((3,3), np.uint8)
    width = 640
    hieght = 480
    channel = 3

    fps = 8
    sec = 10

    fourcc = cv2.VideoWriter_fourcc(*'MP42')

    video = cv2.VideoWriter('image_to_video.avi', fourcc, float(fps), (width, hieght))

    directry = r'C:\Users\diego\Documents\Atividades\Python\VideoErosao\imgs'

    #Iteracoes para o video ficar top
    iteracoes = 1

    for frame_count in range(fps*sec):

        jota = cv2.imread("imgs/" + img + ".jpg")
        img_resize = cv2.resize(jota, (width, hieght))

        if((frame_count%3) == 0):
            imgErosao = cv2.erode(img_resize, kernel, iterations = iteracoes)
            video.write(imgErosao)
            iteracoes += 1
            print(frame_count)

        if((frame_count%3) != 0):
            video.write(imgErosao)
            print(frame_count)

#Função que pega uma imagem e cria um video de dilatacao
def videoDilatacao(img):
    #kernel
    kernel = np.ones((3,3), np.uint8)
    width = 640
    hieght = 480
    channel = 3

    fps = 8
    sec = 10

    fourcc = cv2.VideoWriter_fourcc(*'MP42')

    video = cv2.VideoWriter('image_to_video2.avi', fourcc, float(fps), (width, hieght))

    directry = r'C:\Users\diego\Documents\Atividades\Python\VideoErosao\imgs'

    #Iteracoes para o video ficar top
    iteracoes = 1

    for frame_count in range(fps*sec):

        jota = cv2.imread("imgs/" + img + ".jpg")
        img_resize = cv2.resize(jota, (width, hieght))

        if((frame_count%3) == 0):
            imgDilatacao = cv2.dilate(img_resize, kernel, iterations = iteracoes)
            video.write(imgDilatacao)
            iteracoes += 1
            print(frame_count)

        if((frame_count%3) != 0):
            video.write(imgDilatacao)
            print(frame_count)



def main():

    #variavel pra sair do while
    escape = True

    print("Digite o nome da imagem:", end = ' ')
    img = input()

    while(escape):
        print("Erosao ou Dilatacao meu amigo?")
        escolha = input()
        escolha = escolha.lower()

        #verifica
        if(escolha == "erosao"):
            videoErosao(img)
            escape = False

        elif(escolha == "dilatacao"):
            videoDilatacao(img)
            escape = False

        else:
            print("Digite EROSAO ou DILATACAO por favor.")
            escape = True





if __name__ == "__main__":
	main()
