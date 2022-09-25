import numpy as np
import cv2
from matplotlib import pyplot as plt

def geraImagem(width, height):
    blank_image = np.zeros((height,width,3), np.uint8)
    #Fatiando o vetor em 3 pedaços usando o ":," e mantendo o oque foi pedido
    blank_image[:,width // 3 + width //3:width] = (0,0,255)      # (B, G, R)
    blank_image[:,width // 3:width // 3 + width // 3] = (0,255,0)
    blank_image[:,0:width // 3] = (255,0,0)

    plt.imshow(blank_image)
    plt.show()
    return blank_image

def main():
    filename = "imagem3.png"
    obj_img = geraImagem(600, 300)
    cv2.imwrite(filename, obj_img)

if __name__ == "__main__":
    main()
