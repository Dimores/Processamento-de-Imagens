import cv2
import numpy as np
import matplotlib.pyplot as plt

def showImage(img):
    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():

    min_HSV = np.array([2, 58, 30], dtype = "uint8")
    max_HSV = np.array([240, 255, 240], dtype = "uint8")

    image = cv2.imread("imgs/jonas.jpg")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)
    skinHSV = cv2.bitwise_and(image, image, mask = skinRegionHSV)

    """
    A função numpy.hstack() é usada para empilhar a sequência de arrays de entrada
    horizontalmente (ou seja, coluna sábia) para fazer um único array.
    """
    cv2.imwrite("imgs/hsv.png", np.hstack([image, skinHSV]))
    showImage(skinRegionHSV)

if __name__ == "__main__":
    main()
