import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob

'''
    Observações:
    ->Para trabalhar com a limiarização precisa-se trabalhar com as imagens em PRETO e BRANCO
    ->Precisa-se definir um LIMIAR, que vai controlar a limiarizacao
        .Todos que estiverem abaixo do Limiar irao ficar PRETOS, e acima BRANCOS
    ->Limiarizacao Adaptativa permite que cada regiao possua um limiar proprio
        .Baseada em Média: Pega o pedaço da imagem e calcula a media dele, todo mundo abaixo da media vai ficar preto, e acima branco
        .Baseado em Gaussiana: Representa o pedaço em uma função Gaussiana, calculando a media de todos, considera a media e o desvio padrao


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

def main():
    folder = 'imgs/*'
    image_files_list = glob.glob(folder)

    #Criando as variaveis para as imagens usando a lista do glob
    cartaGetulio = image_files_list[0]
    mapa_1 = image_files_list[1]
    mapa_2 = image_files_list[2]
    mapa_3 = image_files_list[3]

    #Carregando as imagens
    carta_cinza = cv2.imread(cartaGetulio, 0)
    mapa_1_cinza = cv2.imread(mapa_1, 0)



    mapa_2_cinza = cv2.imread(mapa_2, 0)

    eq = cv2.equalizeHist(mapa_2_cinza)

    mapa_3_cinza = cv2.imread(mapa_3, 0)

    #Convertendo as imagens para tons de cinza
    # carta_cinza = cv2.cv2tColor(carta_, cv2.COLOR_BGR2GRAY)
    # mapa_1_cinza = cv2.cv2tColor(mapa_1_, cv2.COLOR_BGR2GRAY)
    # mapa_2_cinza = cv2.cv2tColor(mapa_2_, cv2.COLOR_BGR2GRAY)
    # mapa_3_cinza = cv2.cv2tColor(mapa_3_, cv2.COLOR_BGR2GRAY)

    block_size = 171 #Tamanho da janela em que vao se calcular as regioes, quanto maior mais ele vai considerar
    C = 120 #
    limiar = 180


    ret, thresh_img = cv2.threshold(carta_cinza, 180, 255, cv2.THRESH_BINARY)
    ret, thresh_img1 = cv2.threshold(mapa_1_cinza, limiar, 255, cv2.THRESH_BINARY)  #Vai precisar aplicar um filtro para remover as linha
    medianImg = cv2.medianBlur(thresh_img1, 5)
    medianImg = ~medianImg




    imgAdapMean_3 = cv2.adaptiveThreshold(eq, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)
    _, imgNormThresh_3 = cv2.threshold(mapa_3_cinza, 40, 255, cv2.THRESH_BINARY)
    # imgAdapMean = cv2.adaptiveThreshold(imgOriginal, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)
    # imgAdapGauss = cv2.adaptiveThreshold(imgOriginal, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)


    imgsArray = [thresh_img,  medianImg, imgAdapMean_3, imgNormThresh_3]
    titlesArray = ['THRESH_BINARY', 'THRESH_BINARY', 'ADAPTIVE_THRESH_MEAN_C', 'THRESH_BINARY']
    showMultipleImages(imgsArray, titlesArray, (20, 16), 2, 2)



if __name__ == "__main__":
    main()
