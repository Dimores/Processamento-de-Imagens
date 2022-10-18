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

if __name__ == "__main__":
    main()
