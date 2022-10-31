#Histograma PRETO E BRANCO
#by Diego Morelo
#https://theailearner.com/tag/cv2-comparehist/
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as mt

"""

Faça uma função que receba as imagens S1 e compare ela com S2, D1, D2 e D3 pelo histograma.
Compare a distância de S1 para cada imagem considerando as métricas da Correlação, Chi-Square e Bhattacharrya.
Para cada imagem, some as três distâncias ao quadrado e aplique a raiz quadrada: sqrt(Corr^2 + Chi-Sq^2 + Bhatta^2)
Retorne a imagem mais parecida com S1 (o par que tiver a menor distância)

"""

#Funcao que recebe 5 imagens e compara os seus histogramas com a primeira
def comparaHistograma(S1,S2,D1,D2,D3):
    #Calculando os histogramas de todas as imagens atraves do "cv2.calcHist"
    histS1 = cv2.calcHist([S1], [0], None, [256], [0, 256])
    histS2 = cv2.calcHist([S2], [0], None, [256], [0, 256])
    histD1 = cv2.calcHist([D1], [0], None, [256], [0, 256])
    histD2 = cv2.calcHist([D2], [0], None, [256], [0, 256])
    histD3 = cv2.calcHist([D3], [0], None, [256], [0, 256])
    
    #Normalizando os histogramas
    cv2.normalize(histS1, histS1, alpha = 0, beta = 1, norm_type = cv2.NORM_MINMAX)
    cv2.normalize(histS2, histS2, alpha = 0, beta = 1, norm_type = cv2.NORM_MINMAX)
    
    #---------------------------------------S1 COM S2--------------------------------------
    print("----------------------------------------------")
    print("S1 com S2\n")
    #Correlação
    correlacaoS1S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CORREL)
    print("Correlacao(S1,S2)  :", correlacaoS1S2)
    
    #Chi-Square
    chiSquareS1S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CHISQR)
    print("Chi-Square(S1,S2)  :", chiSquareS1S2)
    
    #Bhattacharyya
    bhattacharyyaS1S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_BHATTACHARYYA)
    print("Bhattacharry(S1,S2):", bhattacharyyaS1S2)
    
    distanciaS1S2 = 0
    distS1S2 = float(distanciaS1S2)
    
    distS1S2 = mt.sqrt(pow(correlacaoS1S2,2) + pow(chiSquareS1S2,2) + pow(bhattacharyyaS1S2,2))
    print("Distancia(S1,S2)   :", distS1S2)
    print("----------------------------------------------")
    #--------------------------------------------------------------------------------------
    
    #---------------------------------------S1 COM D1--------------------------------------
    print("S1 com D1\n")
    #Correlação
    correlacaoS1D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_CORREL)
    print("Correlacao(S1,D1)  :", correlacaoS1D1)
    
    #Chi-Square
    chiSquareS1D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_CHISQR)
    print("Chi-Square(S1,D1)  :", chiSquareS1D1)
    
    #Bhattacharyya
    bhattacharyyaS1D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_BHATTACHARYYA)
    print("Bhattacharry(S1,D1):", bhattacharyyaS1D1)
    
    distanciaS1D1 = 0
    distS1D1 = float(distanciaS1D1)
    
    distS1D1 = mt.sqrt(pow(correlacaoS1D1,2) + pow(chiSquareS1D1,2) + pow(bhattacharyyaS1D1,2))
    print("Distancia(S1,D1)   :", distS1D1)
    print("----------------------------------------------")
    #--------------------------------------------------------------------------------------

def main():

    #Carregando as imagens
    S1 = cv2.imread('imgs/S1.jpg', 0)
    S2 = cv2.imread('imgs/S2.jpg', 0)
    D1 = cv2.imread('imgs/D1.jpg', 0)
    D2 = cv2.imread('imgs/D2.jpg', 0)
    D3 = cv2.imread('imgs/D3.jpg', 0)

    comparaHistograma(S1,S2,D1,D2,D3)
    #Mostrando o histograma e a imagem na tela
    #cv2.imshow("Imagem original", img)
    #plt.show()

    #cv2.waitKey(0)  #Tecla Q
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
