import numpy as np
import cv2
from matplotlib import pyplot as plt

'''
    Observações(FILTROS):
        ->Blur: Blur ou PASSA-BAIXA, retém a alta frequência, passando a baixa frequência
        ->Gaussiano: Borra de um jeito que a parte central da imagem tem mais peso que a vizinhança
        ->Mediana: Ordena os valores dentro do operador de convulaçao, depois pega o elemento do meio
        ->Bilateral: As cores muito diferentes do centro sao menos borradas, preservando as arestas
        ->Sobel: Aplica Gaussiano, passa alta, direção horizontal e vertical, Detecta arestas atraves de derivadas
        ->Laplaciano: Detecta arestas atraves de derivadas(de derivadas), o quanto a variacao esta variando
        ->CannyEdge: Detector de arestas, aplicando sobel, usando limiar minimo e maximo
'''

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


def processImage(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(src = image, code =cv2.COLOR_BGR2GRAY)
    return image


def convolve2d(image, kernel):

    # Inverte a matriz na direção para cima/para baixo. Depois inverte a ordem dos elementos ao longo do eixo 1 (esquerda/direita).
    kernel = np.flipud(np.fliplr(kernel))

    # output da convulacao
    output = np.zeros_like(image) #Retorna uma matriz de zeros com a mesma forma e tipo de uma determinada matriz.

    # Adicionar preenchimento zero à imagem de entrada
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    image_padded[1 : -1, 1 : -1] = image

    # Loop pra cada pixel da imagem
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            # multiplicação elementar do kernel e da imagem
            output[y, x] = (kernel * image_padded[y: y + 3, x: x + 3]).sum() 

    return output


def main():
    img = processImage("imgs/monalisa.jpg")

    # Matriz usada na convulacao(blur)
    matrix = np.array([[0.1, 0.1, 0.1], [0.1, 0.1, 0.1], [0.1, 0.1, 0.1]])

    # Destino
    dest_image = convolve2d(img, kernel)

    imgArray = [img, output]
    titleArray = ["Original", "Blur"]

    showMultipleImages(imgArray, titleArray, (30,26), 2, 1)

if __name__ == "__main__":
    main()
