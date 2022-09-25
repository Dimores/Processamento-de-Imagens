import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

#Função que irá extrair a região de interesse desejada
def crop(img, x, y, width, height):
    croppedImg = img[y : height, x : width]
    return croppedImg

#Função que cola uma imagem menor em uma imagem maior
def paste(src, dst, x, y):
    src[y : y + dst.shape[0], x : x + dst.shape[1]] = dst
    return src

def main():
    messiImg = cv2.imread("imgs/messi.jpg")
    xBola = 336
    yBola = 288
    larguraBola = 388
    alturaBola = 337
    ball = crop(messiImg, xBola, yBola, larguraBola, alturaBola)
    showImage(ball)

    arquivo = "novaImagem.jpg"
    newImg = paste(messiImg, ball, 87, 288)

    #Salvando a nova imagem
    cv2.imwrite(arquivo, newImg)

if __name__ == "__main__":
    main()
