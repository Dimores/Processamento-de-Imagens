import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImageInfo(img):
    altura, largura, canaisDeCor = img.shape
    print("Dimensões da imagem: " + str(largura) + "x" + str(altura))
    print("Canais de cor: " + str(canaisDeCor))

def showImage(img):
    img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def rescaleImage(img, scale):
    print("\n-------Antes-------\n")
    showImageInfo(img)
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print("\n-------Depois-------\n")
    showImageInfo(resized)
    showImage(resized)


def main():

    obj_img = cv2.imread("imgs/Rengoku.jpg")
    rescaleImage(obj_img, 50)


if __name__ == "__main__":
    main()
