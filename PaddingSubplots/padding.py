import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showImageGrid(imgsArray, titlesArray)

    #Tratamento na vertical
    elif(x == 1):
        fig, axis = plt.subplots(y)  #y será o total de linhas, e x = 1
        fig.suptitle(titlesArray)   #Centraliza o título entre as imagens
        yId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId].imshow(imgMPLIB)  #

            yId += 1

    #Tratamento na horizontal
    elif(y == 1):
        fig, axis = plt.subplots(1, x) #Exibindo 1 linha de imagens, x = número de colunas
        fig.suptitle(titlesArray)     #Centralizar o título na coluna de linhas
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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

def plotSingleImage():
    #Criando grid com a imagem original apenas
    imgOriginal = cv2.imread("Imgs/Rengoku.jpg")
    showImageGrid(imgOriginal, "Rengoku")

def plotTwoImageVertical():
    imgOriginal = cv2.imread("imgs/Rengoku.jpg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 200, 100, 50, 10, cv2.BORDER_REPLICATE)

    #Criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    showMultipleImageGrid(imgsArray, title, 1, 2)

def plotThreeImages():
    imgOriginal = cv2.imread("imgs/Rengoku.jpg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE) #Replica os pixel em 4 direções
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)    #Espelho

    #np.ones cria uma matriz só com o número 1, com a altura e largura da imagem original, com 4 canais de cores(R, G, B, A)
    #A = Alfa -> se A = 0(imagem normal), se A = 255(transparência máxima)
    imgTransparent = np.ones((imgOriginal.shape[0], imgOriginal.shape[1], 4), np.uint8) * 255  #Matriz retangular

    #Criando grid com 3 imagens, a segunda com borda replicada e a terceira com borda de espelho
    #A ultima imagem é transparente
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgTransparent]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', '']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)  #2 elementos na linha de cima e 2 na de baixo

def plotFourImages():
    imgOriginal = cv2.imread("imgs/Rengoku.jpg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101) #Outro tipo de espelho

    #Criando grid com 4 imagens, a segunda com borda replicada e a terceira e quarta com borda de espelho
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101] #Colocando as 4 imagens em um array
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 2']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def plotSixImages():
    imgOriginal = cv2.imread("imgs/Rengoku.jpg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
    imgWrap = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_WRAP)

    burgundy = [31, 2, 141]   # (B, G, R)
    imgConstant = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value = burgundy) #Borda de moldura com a cor informada

    #Criando grid com 6 imagens, a segunda com borda replicada e a terceira e quarta com borda de espelho
    #Constant insere uma moldura e wrap só olhando pra entender =)
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101, imgConstant, imgWrap]  #Vetor de imagens
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 2', 'Moldura', 'Efeito Wrap'] #Vetor de títulos
    showMultipleImageGrid(imgsArray, titlesArray, 3, 2)  #X = 3 e Y = 2

def showImageGrid(img, title):
    #Subplots são subáreas dentro da área maior
    fig, axis = plt.subplots()      #axis é cada subplot(matriz de subplots)
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)  #Exibe a imagem dentro do meu subplot
    axis.set_title(title)  #Coloca um título no subplot
    plt.show()             #Mostra tudo dentro do canvas

def plotTwoImageHorizontal():
    imgOriginal = cv2.imread("imgs/Rengoku.jpg")
    #Cria uma uma borda ao redor da imagem do tamanho que quiser
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

    #Criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    showMultipleImageGrid(imgsArray, title, 2, 1)   #X = 2, Y = 1 -> Horizontal

def main():
    plotSixImages()

if __name__ == "__main__":
    main()
