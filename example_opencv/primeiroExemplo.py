import numpy as np
import cv2
from matplotlib import pyplot as plt

#imread() carrega a imagem na estrutura de dados
obj_img = cv2.imread("imgs/Tanjiro.jpeg")
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
plt.imshow(obj_img)
plt.show()
