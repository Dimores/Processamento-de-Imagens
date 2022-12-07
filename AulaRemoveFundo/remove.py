from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

'''
    Observações>
    1->Implementar interface gráfica antes do Grab Cut


'''

#Faz a sobreposição de duas imagens
def addImageOverlay(background, foreground, translationForegroundW, translationForegroundH):

    #Pegando a altura e a largura da imagem da frente e da de trás
    backH, backW, _ = background.shape
    foreH, foreW, _ = foreground.shape

    #Subtraindo altura e largura da imagem, e pegando "oque sobra"
    remainingH, remainingW = backH - foreH, backW - foreW

    #Se a posição y da imagem normal + a altura dela forem maiores do que a altura da imagem de fundo
    if translationForegroundH + foreH > backH:
        print("Erro: Sobreposição com altura maior do que a permitida.")
        print("Posição final que altura do objeto da frente termina:", translationForegroundH + foreH)
        print("Altura do fundo:", backH)
        return

    #Se a posição x da imagem normal + a largura dela forem maiores do que a largura da imagem de fundo
    if translationForegroundW + foreW > backW:
        print("Erro: sobreposição com largura maior do que a permitida.")
        print("Posição final que largura do objeto da frente termina:", translationForegroundW + foreW)
        print("Largura do fundo:", backW)
        return

    #Parte do cenário do fundo em que a imagem será adicionada
    crop = background[translationForegroundH : foreH + translationForegroundH, translationForegroundW : foreW + translationForegroundW]

    #Transformamos o foreground em imagem com tons de cinza e criamos uma máscara binária da mesma com a binarização (cv2.threshold)
    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY) #Separa os pixels que compoem a imagem do fundo
    ret, maskFore = cv2.threshold(foregroundGray, 210, 255, cv2.THRESH_BINARY)  #Linearização

    #Agora aplicamos uma operação de AND binário na imagem recortada 'crop'. No caso, realizar a operação binária entre a mesma imagem não terá efeito. Só que, com a inclusão da máscara no terceiro parâmetro, os pixels pretos de maskFore serão ignorados e, portanto, ficarão escuros. Com isso temos a marcação em que vamos incluir o foreground posteriormente.
    backWithMask = cv2.bitwise_and(crop, crop, mask = maskFore)
    foreWithMask = cv2.bitwise_not(maskFore)
    foreWithMask = cv2.bitwise_and(foreground, foreground, mask = foreWithMask)

    #Faremos a composição entre 'frente' e 'fundo', compondo o foreground na imagem extraída do background.
    combinedImage = cv2.add(foreWithMask, backWithMask)

    #Adicionamos a imagem gerada no background final.
    copyImage = background.copy()
    copyImage[translationForegroundH:foreH + translationForegroundH, translationForegroundW:foreW + translationForegroundW] = combinedImage

    return copyImage

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

def showMultipleImages(imgsArray, titlesArray, size, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showSingleImage(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y, figsize = size)
        yId = 0
        for img in imgsArray:
            axis[yId].imshow(img, 'gray')
            axis[yId].set_anchor('NW')
            axis[yId].set_title(titlesArray[yId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x, figsize = size)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            axis[xId].imshow(img, 'gray')
            axis[xId].set_anchor('NW')
            axis[xId].set_title(titlesArray[xId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x, figsize = size)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            axis[yId, xId].set_title(titlesArray[titleId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)
            axis[yId, xId].set_anchor('NW')
            axis[yId, xId].imshow(img, 'gray')
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def carregaImagemCinza(img):
    img = cv2.imread(img, 0)
    return img

class GrabCutGUI(Frame): #Frame é a classe pai
    def __init__(self, master = None):
        #Invoca o construtor da classe pai Frame
        Frame.__init__(self, master)  #Self refere-se a instancia do objeto

        #Inicializar a interface gráfica
        self.iniciaUI()

    def iniciaUI(self):
        #preparando a janela
        self.master.title("Janela da Imagem Segmentada")
        self.pack()  #Pega os componentes que a sua janela tem até o momento, e organiza

        #computa ações de mouse
        self.computaAcoesDoMouse()

        #carregando a imagem do disco
        self.imagem = self.carregaImagemASerExibida()

        #criar um canvas que receberá a imagem
        self.canvas = Canvas(self.master, width = self.imagem.width(), height = self.imagem.height(), cursor = "cross")

        #desenhar a imagem que carreguei no canvas
        self.canvas.create_image(0, 0, anchor = NW, image = self.imagem)
        self.canvas.image = self.imagem #pra imagem não ser removida pelo garbage collector

        #posiciona todos os elementos no canvas
        self.canvas.pack()

    def computaAcoesDoMouse(self):
        self.startX = None
        self.startY = None
        self.rect   = None

        self.master.bind("<ButtonPress-1>", self.callbackBotaoPressionado)
        self.master.bind("<B1-Motion>", self.callbackBotaoPressionadoEmMovimento)
        self.master.bind("<ButtonRelease-1>", self.callbackBotaoSolto)

    def callbackBotaoSolto(self, event):
        if self.rectangleReady:
            #criar uma nova janela
            windowGrabcut = Toplevel(self.master)
            windowGrabcut.wm_title("Segmentation")
            windowGrabcut.minsize(width = self.imagem.width(), height = self.imagem.height())

            #criar canvas pra essa nova janela
            canvasGrabcut = Canvas(windowGrabcut, width = self.imagem.width(), height = self.imagem.height())
            canvasGrabcut.pack()

            #aplicar grabcut na imagem
            mask = np.zeros(self.imagemOpenCV.shape[:2], np.uint8)
            print(mask.shape)
            rectGcut = (int(self.startX), int(self.startY), int(event.x - self.startX), int(event.y - self.startY))
            fundoModel = np.zeros((1, 65), np.float64)
            objModel = np.zeros((1, 65), np.float64)

            #invocar grabcut
            cv2.grabCut(self.imagemOpenCV, mask, rectGcut, fundoModel, objModel, 5, cv2.GC_INIT_WITH_RECT)
            #imagemOpenCv = cv2.blur(imagemOpenCV, (15,15))

            #preparando imagem final
            maskFinal = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
            imgFinal = self.imagemOpenCV * maskFinal[:,:,np.newaxis]
            for x in range(0, self.imagemOpenCV.shape[1]):
                for y in range(0, self.imagemOpenCV.shape[0]):
                    if(maskFinal[y][x] == 0):
                        imgFinal[y][x][0] = imgFinal[y][x][1] = imgFinal[y][x][2] = 0

            #converter de volta do opencv pra Tkinter
            imgFinal = cv2.cvtColor(imgFinal, cv2.COLOR_BGR2RGB)
            imgFinal = Image.fromarray(imgFinal)
            imgFinal = ImageTk.PhotoImage(imgFinal)

            #inserir a imagem segmentada no canvas
            canvasGrabcut.create_image(0, 0, anchor = NW, image = imgFinal)
            canvasGrabcut.image = imgFinal

    def callbackBotaoPressionadoEmMovimento(self, event):
        #novas posicoes de x e y
        currentX = self.canvas.canvasx(event.x)
        currentY = self.canvas.canvasy(event.y)

        #atualiza o retângulo a ser desenhado
        self.canvas.coords(self.rect, self.startX, self.startY, currentX, currentY)

        #verifica se existe retângulo desenhado
        self.rectangleReady = True

    def callbackBotaoPressionado(self, event):
        #convertendo o x do frame, pro x do canvas e copiando isso em startX
        self.startX = self.canvas.canvasx(event.x)
        self.startY = self.canvas.canvasy(event.y)

        if not self.rect:
            self.rect = self.canvas.create_rectangle(0, 0, 0, 0, outline="blue")

    def carregaImagemASerExibida(self):
        caminhoDaImagem = filedialog.askopenfilename()

        #se a imagem existir, entra no if
        if(len(caminhoDaImagem) > 0):
            self.imagemOpenCV = cv2.imread(caminhoDaImagem)

            #converte de opencv para o formato PhotoImage
            image = cv2.cvtColor(self.imagemOpenCV, cv2.COLOR_BGR2RGB)

            #converte de OpenCV pra PIL
            image = Image.fromarray(image)

            #converte de PIL pra PhotoImage
            image = ImageTk.PhotoImage(image)

            return image


def main():
    #Inicializando a Tkinter
    root = Tk()

    #Cria a aplicação
    appcut = GrabCutGUI(master = root)

    #Cria um loop do programa
    appcut.mainloop()

if __name__ == "__main__":
    main()
