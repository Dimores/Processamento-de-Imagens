"""
Pegue duas fotos (uma normal e outra com o cabelo
marcado com uma máscara) e faça um algoritmo
para mudar a cor de cabelo.
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def resizeImage(img, scalePercent):
    width = int(img.shape[1] * scalePercent / 100)
    height = int(img.shape[0] * scalePercent / 100)

    img = cv2.resize(img, (width, height))

    return img

def showMultipleImageGrid(imgsArray, titlesArray, x, y):

    #Verifica se x e y são zero
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return

    #Se x e y forem 1
    elif(x == 1 and y == 1):
        showImageGrid(imgsArray, titlesArray)

    #Tratamento na vertical
    elif(x == 1):
        fig, axis = plt.subplots(y)  #y será o total de linhas, e x = 1
        fig.suptitle(titlesArray)   #Centraliza o título entre as imagens
        yId = 0

        #Para cada imagem no vetor
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Converte a imagem pra RGB
            axis[yId].imshow(imgMPLIB)  #Mostra a imagem para cada Y

            yId += 1

    #Tratamento na horizontal
    elif(y == 1):
        fig, axis = plt.subplots(1, x) #Exibindo 1 linha de imagens, x = número de colunas
        fig.suptitle(titlesArray)     #Centralizar o título na coluna de linhas
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Converte a imagem para RGB
            axis[xId].imshow(imgMPLIB)  #Exibindo a imagem na posição x na minha grade

            xId += 1

    #Grids (2,2) em diante: (3,3); (4,4)...
    else:
        fig, axis = plt.subplots(y, x)  #Invocando os subplot passando total de linhas e colunas
        xId, yId, titleId = 0, 0, 0    #Contadores para x, y e títulos
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Convertendo todas as imagens para as cores certas
            axis[yId, xId].set_title(titlesArray[titleId])   #Para todos os subplots, passar o título da posição
            axis[yId, xId].imshow(imgMPLIB)                  #Exibindo a imagem da posição

            #Quando o total de caracteres que o título tem for 0
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')  #Desligar os eixos daquele subplot

            titleId += 1  #Próximo título
            xId += 1      #Próxima posição em x
            if xId == x:  #Limitando o greed x
                xId = 0
                yId += 1  #Andando no eixo y

        fig.tight_layout(pad=0.5) #Controla a janela e diminui as distâncias entre os elemtos
    plt.show()

def plotAddedImages():
    max = cv2.imread("imgs/max.jpg")
    maxMask = cv2.imread("imgs/maxMask.jpg")
    # addedImage = cv2.add(max, maxMask)  #Soma duas imagens
    addedWeightedImage = cv2.addWeighted(max, 0.5, maxMask, 0.5, 1) #Soma ponderada de 2 imagens, utilizando porcentagem

    imgTransparent = np.ones((max.shape[0], max.shape[1], 4), np.uint8) * 255  #Matriz retangular, imagem para preencher buraco

    #Criando grid com 3 imagens, primeira normal a segunda com máscara e a terceira com addWeight
    #a ultima imagem é transparente
    imgsArray = [max, maxMask, addedWeightedImage, imgTransparent] #Vetor de imagens
    titlesArray = ['Max', 'Máscara', 'cv2.addWeighted', '']  #Vetor de títulos
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)  #Mostrando imagens na tela

def main():
    plotAddedImages()

if __name__ == "__main__":
    main()
