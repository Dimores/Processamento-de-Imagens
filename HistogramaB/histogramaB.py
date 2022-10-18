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
    img = cv2.imread('imgs/universe.jpg') #Carregando a imagem colorida

    #Criando uma lista com 3 elementos
    color = ('b', 'g', 'r')

    #"col" vai receber b, depois g, depois r
    #"enumerate()" é util na passagem de parâmetros para construir cada histograma
    for i, col in enumerate(color): #For que vai iterar para cada canal
        histograma = cv2.calcHist([img], [i], None, [256], [0,256]) #Função que gera os 3 histogramas separados("None" = máscara)
        plt.plot(histograma, color = col)    #Função que constroi o histograma definido, para o canal de cor específico
        plt.xlim([0,256])    #Definindo os limites em relação a X desse histograma

    #Exibindo a imagem e o histograma
    cv2.imshow("Imagem original", img)
    plt.show()

    cv2.waitKey(0) #Tecla Q
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
