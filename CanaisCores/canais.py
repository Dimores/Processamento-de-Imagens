import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def tiraMedia(largura, altura, c1, c2, c3):
    #Usando a função np.sum() que soma todos os elementos da matriz
    a = c1.sum()
    b = c2.sum()
    c = c3.sum()

    #Pegando o número total de pixels
    numPixels = largura * altura
    a = a // numPixels
    b = b // numPixels
    c = c // numPixels

    print("Média de azul por pixel     = ", a)
    print("Média de verde por pixel    = ", b)
    print("Média de vermelho por pixel = ", c)

    if((a > b) and (a > c)):
        print("\nA imagem é mais AZUL!")
    if((b > a) and (b > c)):
        print("\nA imagem é mais VERDE!")
    if((c > a and (c > b)):
        print("\nA imagem é mais VERMELHA")

def main():
    #
    # #Variáveis para cor
    # azul = 0
    # verde = 1
    # vermelho = 2

    imagem = cv2.imread("imgs/passaro.jpg")
    altura, largura, canaisDeCor = imagem.shape

    #Dividindo cada canal de cor em um vetor
    b, g, r = cv2.split(imagem)
    # print(b)

    tiraMedia(largura, altura, b, g, r)

    cv2.imshow("Imagem azul", b)        #azul
    cv2.imshow("Imagem verde", g)       #verde
    cv2.imshow("Imagem vermelha", r)    #vermelho

    cv2.waitKey(0)
    # img1 = extraiCanalCor(imagem, altura, largura, azul, verde)
    # # showImage(img1)
    # img1V = criaVetor(img1, altura, largura, vermelho)

    # voltaImagemNormal(imagem, altura, largura)
    # showImage(imagem)

    # img2 = extraiCanalCor(imagem, altura, largura, azul, vermelho)

if __name__ == "__main__":
    main()
