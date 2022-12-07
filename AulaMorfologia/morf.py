import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob

'''
    Observações(Filtros Morfológicos):
        1->Erosão: Diminuir o volume de pixels(afinada na imagem) dependendo do operador morfológico, desconectando objetos.
        2->Dilatação: Reparar quebras, reparar intrusões, dilata a imagem(engorda a imagem)

        3->Abertura: Uso de erosão e dilatação juntos, reduzindo pequenos ruidos
        4->Fechamento: Uso de erosão e dilatação juntos, porém na ordem contrario da abertura

        5->Gradiente morfologico: Diferença entra dilatacao e erosao da imagem, encontra os contornos da imagem



'''

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

def showMultipleImages(imgsArray, titlesArray, size, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showSingleImage(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y, figsize = size)
        yId = 0
        for img in imgsArray:
            axis[yId].imshow(img, 'gray')
            axis[yId].set_anchor('NW')
            axis[yId].set_title(titlesArray[yId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x, figsize = size)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            axis[xId].imshow(img, 'gray')
            axis[xId].set_anchor('NW')
            axis[xId].set_title(titlesArray[xId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x, figsize = size)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            axis[yId, xId].set_title(titlesArray[titleId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)
            axis[yId, xId].set_anchor('NW')
            axis[yId, xId].imshow(img, 'gray')
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def carregaImagemCinza(img):
    img = cv2.imread(img, 0)
    return img

#Funcao que aplica a erosao em imagens preto e branco
def aplicaErosao(img, iteracoes):
    #Criando a kernel
    kernel = np.ones((4,4), np.uint8)

    #Aplicando a erosao
    imgErosao = cv2.erode(img, kernel, iterations = iteracoes)
    return imgErosao

#Funcao que aplica a dilatacao em imagens preto e branco
def aplicaDilatacao(img, iteracoes):
    #Criando a kernel
    kernel = np.ones((4,4), np.uint8)

    #Aplicando a dilatacao
    imgErosao = cv2.dilate(img, kernel, iterations = iteracoes)
    return imgErosao

#Função que aplica abertura(na mao)
def aplicaAbertura(img, iteracoes):
    #Criando a kernel
    kernel = np.array([[0,1,1,0], [1,1,1,1], [0,1,1,0]], np.uint8)

    #Aplicando a abertura
    erosion = cv2.erode(img, kernel, iterations = iteracoes)
    dilate = cv2.dilate(erosion, kernel, iterations = iteracoes)
    return dilate

#Função que aplica fechamento(usando funcao)
def aplicaFechamento(img):
    #Criando a kenel
    kernel = np.ones((11,11), np.uint8)

    fechamento = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return fechamento

def aplicaGradienteMorfologico(img):
    #Criando a kernel
    kernel = np.ones((2,2), np.uint8)

    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    return gradient

def main():
    folder = 'imgs/*'
    image_files_list = glob.glob(folder)

    #Criando as variaveis para as imagens usando a lista do glob
    mickey = image_files_list[0]
    veado = image_files_list[1]
    bolas = image_files_list[2]

    #Carregando as imagens em tons de cinza
    mickey = carregaImagemCinza(mickey)
    veado = carregaImagemCinza(veado)
    bolas = carregaImagemCinza(bolas)

    #Fazendo um threshold no mickey
    ret, mickeyThreshold = cv2.threshold(mickey, 127, 255, cv2.THRESH_BINARY_INV)

    #Aplicando a erosao na imagem
    #imgErodida = aplicaErosao(mickeyThreshold, 8) #2 iterecoes

    imgAbertura = aplicaAbertura(veado, 3)
    imgAbertura2 = aplicaAbertura(bolas, 4)

    #imgFechamento = aplicaFechamento(imgAbertura)

    gradient = aplicaGradienteMorfologico(mickeyThreshold)

    imgArray = [mickeyThreshold, gradient, veado, imgAbertura, bolas, imgAbertura2]
    titlesArray = ['Original', 'Gradient', 'Original', 'Abertura', 'Original', 'Abertura']
    showMultipleImages(imgArray, titlesArray, (20,16), 2, 3)


if __name__ == "__main__":
    main()
