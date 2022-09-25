import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    imgMPLIB =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def drawTriangle(img, p1, p2, p3):
    #Desenhando o triângulo com a ajuda de linhas
    #na janela preta Com pontos dados
    #cv2.line é a função embutida na biblioteca opencv
    cv2.line(img, p1, p2, (0, 0, 0), 3)
    cv2.line(img, p2, p3, (0, 0, 0), 3)
    cv2.line(img, p1, p3, (0, 0, 0), 3)

    #Definindo uma matriz de extremidades do triângulo
    points = np.array([[p1], [p2], [p3]])

    # Use a função fillPoly() e dê entrada como
    #imagem, pontos finais, cor do triângulo
    # Aqui a cor do triângulo será PRETA
    cv2.fillPoly(img, pts=[points], color=(0, 0, 0))
    return img

def getColor(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)
    return img

def main():
    imgOpenCv = cv2.imread("imgs/Babuino.jpg")
    altura, largura, canalCor = imgOpenCv.shape

    for y in range(0, altura):
        for x in range(0, largura):
            azul, verde, vermelho = getColor(imgOpenCv, x, y)
            imgOpenCv = setColor(imgOpenCv, x, y, azul, verde, vermelho)

    #Desenhe três linhas que passam pelos pontos dados usando a função de linha embutida do OpenCV. Ele irá criar um triângulo na janela preta.
    #Encontre o baricentro do triângulo usando a fórmula do centróide.
    p1 = (607, 238)
    p2 = (776, 238)
    p3 = (690, 96)
    novaImg = drawTriangle(imgOpenCv, p1,p2,p3)

    arquivo = "triangulo.jpg"

    cv2.imwrite(arquivo, novaImg)
    showImage(novaImg)

if __name__ == "__main__":
    main()
