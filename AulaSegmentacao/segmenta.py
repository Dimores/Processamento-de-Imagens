import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
    Observações(K-Means):
        1->Quantização: Representar a informação por quantias ou quantidades menores(reduzindo cores por ex)
        2->Segmentação: Identificar um segmento da imagem de seu interesse(por ex identificar orgão em imagens médicas)

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

def transform8Bits(img):

    #Get input size
    height, width = img.shape[:2]

    #Desired "pixelated" size
    w, h = (40, 40)

    #Resize input to "pixelated" size
    temp = cv2.resize(img, (w, h), interpolation = cv2.INTER_LINEAR)

    #Initialize output image
    output = cv2.resize(temp, (width, height), interpolation = cv2.INTER_NEAREST)

    return output

def computeKmeans(img, cores):
    #Converter a imagem para uma matriz Z
    Z = img.reshape((-1, 3)) #Mudar as dimensões da imagem original(altura, quantidade de colunas)
    Z = np.float32(Z)

    #Critério para interromper o Kmeans
    criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.1)

    #Quantidade de cores que a imagem vai ter
    K = cores

    _, labels, centroides = cv2.kmeans(Z, K, None, criterio, 10, cv2.KMEANS_RANDOM_CENTERS)

    centroides = np.uint8(centroides)
    imagemColoridaComCentroides = centroides[labels.flatten()] #Pega a matriz quadrada e transforma em um vetor de 1 dimensão

    imagemFinal = imagemColoridaComCentroides.reshape((img.shape))

    return imagemFinal


def main():
    img = cv2.imread("imgs/1.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img2 = cv2.imread("imgs/2.jpg")

    img2 = computeKmeans(img2, 1)
    showSingleImage(img2, "MuitoBoa", (20,16))

    # img2 = transform8Bits(img)
    #
    # #Gerando a imagem 8 bits novamente usando o Kmeans
    # imgKmeans = computeKmeans(img2)

    # imgArray = [img, img2, img2, imgKmeans]
    # titlesArray = ['Original', '8 bits', '8 bits', 'Kmeans']
    #
    # showMultipleImages(imgArray, titlesArray, (20,16), 2, 2)


if __name__ == "__main__":
    main()
