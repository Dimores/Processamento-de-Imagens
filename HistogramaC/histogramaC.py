#Histograma COLORIDO
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""

Observações importantes no histograma(colorido):
    ->Precisa-se construir 1 histograma para cada canal de cor
    ->Tons mais claros de cor são localizados a direita
    ->Tonas mais escuros de cor são localizados a esquerda

"""

def main():
    imgBgr = cv2.imread("imgs/escura.jpg")

    #Convertendo a imagem para HSV
    imgHsv = cv2.cvtColor(imgBgr, cv2.COLOR_BGR2HSV)
    imgHsv[:, :, 2] = cv2.equalizeHist(imgHsv[:, :, 2])# O canal V no espaço de cores HSV
    saida = cv2.cvtColor(imgHsv, cv2.COLOR_HSV2BGR) #Convertendo a imagem de volta para BGR
    concat = cv2.hconcat((imgBgr,saida))   #Concatenando a imagem com a imagem equalizada
    cv2.imwrite("equalizeHist.jpg",concat)

    color = ('b', 'g', 'r')

    #"col" vai receber b, depois g, depois r
    #"enumerate()" é util na passagem de parâmetros para construir cada histograma
    for i, col in enumerate(color): #For que vai iterar para cada canal
        histograma = cv2.calcHist([imgBgr], [i], None, [256], [0,256]) #Função que gera os 3 histogramas separados("None" = máscara)
        plt.plot(histograma, color = col)    #Função que constroi o histograma definido, para o canal de cor específico
        plt.xlim([0,256])    #Definindo os limites em relação a X desse histograma

    plt.show()

    #"col" vai receber b, depois g, depois r
    #"enumerate()" é util na passagem de parâmetros para construir cada histograma
    for i, col in enumerate(color): #For que vai iterar para cada canal
        histograma2 = cv2.calcHist([concat], [i], None, [256], [0,256]) #Função que gera os 3 histogramas separados("None" = máscara)
        plt.plot(histograma2, color = col)    #Função que constroi o histograma definido, para o canal de cor específico
        plt.xlim([0,256])    #Definindo os limites em relação a X desse histograma

    plt.show()

    cv2.waitKey(0) #Tecla Q
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
