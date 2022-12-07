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

#Função que aplica o filtro escolhido em uma Imagem
def aplicaFiltro(img, filtro):
    if((filtro == "media") or (filtro == "Media") or (filtro == "MEDIA")): #Se oque foi digitado e media
        blurImg = cv2.blur(img, (15, 15))
        return blurImg

    elif((filtro == "gaussiano") or (filtro == "Gaussiano") or (filtro == "GAUSSIANO")): #Se oque foi digitado e gaussiano
        gausImg = cv2.GaussianBlur(img, (15, 15) , 2)
        return gausImg

    elif((filtro == "mediana") or (filtro == "Mediana") or (filtro == "MEDIANA")): #Se oque foi digitado e mediana
        medianImg = cv2.medianBlur(img, 5)
        return medianImg

    elif((filtro == "bilateral") or (filtro == "Bilateral") or (filtro == "BILATERAL")): #Se oque foi digitado e bilateral
        bltImg = cv2.bilateralFilter(img, 9, 75, 75)  #Primeiro sigma espacial, o segundo das cores
        return bltImg

    elif((filtro == "sobel") or (filtro == "Sobel") or (filtro == "SOBEL")):
        cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        sobImgX = cv2.Sobel(src = cinza, ddepth = cv2.CV_64F, dx=1, dy=0, ksize=3)
        sobImgY = cv2.Sobel(src = cinza, ddepth = cv2.CV_64F, dx=0, dy=1, ksize=3)
        #Somando X e Y
        sobImgXY = cv2.addWeighted(sobImgX, 0.5, sobImgY, 0.5, 0) #melhor usar assim
        return sobImgXY

    elif((filtro == "laplaciano") or (filtro == "Laplaciano") or (filtro == "LAPLACIANO")):
        cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        lapImg = cv2.Laplacian(cinza, cv2.CV_64F, ksize=3)
        return lapImg

    elif((filtro == "canny") or (filtro == "Canny") or (filtro == "CANNY")):
        cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cinza = cv2.GaussianBlur(cinza, (3, 3), 3, 3)
        canImg = cv2.Canny(cinza, 0, 100)
        return canImg

    else:
        print("Informe o nome do filtro novamente:", end = '')
        filtro = input()
        imgErr = aplicaFiltro(img, filtro)
        imgsArray = [img, imgErr]
        titlesArray = ['Original', filtro]
        showMultipleImages(imgsArray, titlesArray, (30, 26), 2, 1)

def main():
    img = cv2.imread("imgs/monalisa.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print("Escolha o filtro:")
    print("OPCOES: 'media', 'mediana', 'gaussiano', 'bilateral', 'sobel', 'laplaciano', 'canny'", end = ': ')
    filtro = input()

    img2 = aplicaFiltro(img, filtro)

    imgsArray = [img, img2]
    titlesArray = ['Original', filtro]
    showMultipleImages(imgsArray, titlesArray, (30, 26), 2, 1)


if __name__ == "__main__":
    main()
