import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

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

def main():
    #Criando a lista de arquivo do glov
    folder = 'imgs/*'
    image_files_list = glob.glob(folder)

    caraBonito = image_files_list[0]
    caraBonito = cv2.imread(caraBonito)
    caraBonito = cv2.cvtColor(caraBonito, cv2.COLOR_BGR2RGB) #Carregando a imagem e convertendo para RGB

    #Criando uma cópia da imagem original
    fundo = caraBonito.copy()

    mask = np.zeros(caraBonito.shape[:2],np.uint8) #Criando uma mascara da imagem original, cortando tudo exceto as cores

    bgdModel = np.zeros((1,65),np.float64)  #Modelo de fundo, matriz com 0's, que tem um vetor de 65 escalares, cada posicao é um float64
    fgdModel = np.zeros((1,65),np.float64)  #Modelo de objeto, matriz com 0's, que tem um vetor de 65 escalares, cada posicao é um float64

    #Altura e largura para criar o retangulo do grabcut
    altura = int(caraBonito.shape[0])
    largura = int(caraBonito.shape[1])

    #Retangulo que marca a posicao inicial e final aonde o algoritmo será aplicado
    rect = (0, 0, altura, largura)

    cv2.grabCut(caraBonito, mask, rect, bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)

    #Máscara final, em cada posicao da mascara aonde é fundo e provavelmente fundo, ele substitui por 0, do contrário 1
    mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')

    #Multiplicando a imagem pela mascara2, pegando uma matriz em que cada posicao é um vetor 1D,
    #e convertendo cada posicao em um vetor 3D, tornando o fundo preto
    caraBonito = caraBonito * mask2[:,:,np.newaxis]

    #Criando o meu fundo
    for x in range(0, caraBonito.shape[1]):
        for y in range(0, caraBonito.shape[0]):
            if(mask2[y][x] == 1): #Aonde está a mascara, subtrair o fundo - imagemOriginal
                fundo[y][x] -= caraBonito[y][x]


    #Criando uma copia pra borrar o fundo
    copia = fundo.copy()
    copia = cv2.blur(fundo, (30,30))

    #Somando o fundo com a imagem original
    imgFinal = caraBonito + copia

    imgsArray = [caraBonito, mask2, fundo, copia, imgFinal] #Vetor de imagens
    titlesArray = ['Original', 'Mascara', 'fundo', 'blur', 'final']  #Vetor de títulos
    showMultipleImages(imgsArray, titlesArray, (20,16), 2, 3)

if __name__ == "__main__":
    main()
