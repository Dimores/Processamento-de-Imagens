#Histograma PRETO E BRANCO
#by Diego Morelo
import cv2
import numpy as np
from matplotlib import pyplot as plt

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
    
    #Correlação
    correlacao = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CORREL)
    print("Correlacao(S1,S2)  :", correlacao)
    
    #Chi-Square
    chiSquare = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CHISQR)
    print("Chi-Square(S1,S2)  :", chiSquare)
    
    #Bhattacharyya
    bhattacharyya = cv2.compareHist(histS1, histS2, cv2.HISTCMP_BHATTACHARYYA)
    print("Bhattacharry(S1,S2):", bhattacharyya)
        

def main():

    #Carregando as imagens em tons de cinza
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
