import numpy as np
import cv2

def showImage(img):
    from matplotlib import pyplot as plt
    imgMPLIB =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def saveRedImage(img, filename):
    altura, largura, canais = img.shape #shape mostra as dimensões da matriz
    for y in range(0, altura):
        for x in range(0, largura):
            azul = img.item(y, x, 0) #0 é a cordenada azul do pixel
            verde = img.item(y, x, 1) #0 é a cordenada verde do pixel
            vermelho = img.item(y, x, 2) #0 é a cordenada vermelho do pixel

            #print(x, y, ":", vermelho, verde, azul)
            img.itemset((y, x, 1), 2)
            img.itemset((y, x, 0), 2)
    cv2.imwrite(filename, img)

def main():
    imgOpenCv = cv2.imread("imgs/Kokushibou.jpg")
    saveRedImage(imgOpenCv, "novaImagemKokushibou.jpg")
    showImage(imgOpenCv)

if __name__ == "__main__":
    main()
