import numpy as np
import cv2
# import time
from tqdm import tqdm

ESCAPE_KEY_ASCII = 27

def resizeImage(img, scalePercent):
    width = int(img.shape[1] * scalePercent / 100)
    height = int(img.shape[0] * scalePercent / 100)

    img = cv2.resize(img, (width, height))

    return img

def onChange(value):
    #print("valor alterado", value)
    pass

def main():
    #imagem carregada e sua cópia
    img = cv2.imread("imgs/zenitsu.jpg")
    img = resizeImage(img, 64)
    copyimg = img.copy()

    #cria janela gráfica para inserir a imagem
    windowTitle = "Ajuste de Brilho e Contraste"
    cv2.namedWindow(windowTitle)

    #cria trackbar
    cv2.createTrackbar("Contraste", windowTitle, 100, 100, onChange)
    cv2.createTrackbar("Brilho", windowTitle, 0, 200, onChange)

    before_contrast = 100
    update_contrast = False

    before_brightness = 0
    update_brightness = False

    while True:
        current_contrast = cv2.getTrackbarPos("Contraste", windowTitle)
        current_brightness = cv2.getTrackbarPos("Brilho", windowTitle)

        #valor de contraste do trackbar foi alterado pelo usuário
        if before_contrast != current_contrast:
            update_contrast = True
            before_contrast = current_contrast

        #valor de brilho do trackbar foi alterado pelo usuário
        if before_brightness != current_brightness:
            update_brightness = True
            before_brightness = current_brightness

            #se tiver sido marcado que é pra atualizar contraste ou brilho
        if update_contrast == True or update_brightness == True:

            copyimg = cv2.convertScaleAbs(img, alpha = current_contrast / 100, beta = current_brightness) #Método que aplica uma mudança em toda matriz

            update_contrast = False
            update_brightness = False

        cv2.imshow(windowTitle, copyimg)

        keyPressed = cv2.waitKey(1) & 0xFF #cv2.waitKey(1) & 111111
        if keyPressed == ESCAPE_KEY_ASCII:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
