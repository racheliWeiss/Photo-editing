import cv2
from PIL import Image, ImageDraw, ImageFont
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import random

xx, yy = 0, 0

class myimage:
    def __init__(self, nameWindow):
        self.__nameWindow = nameWindow
        self.__img = ""
        self.__file_name = ""
        self.list = [cv2.AKAZE_DESCRIPTOR_MLDB_UPRIGHT, cv2.AKAZE_DESCRIPTOR_MLDB, cv2.AGAST_FEATURE_DETECTOR_THRESHOLD,
                     cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2HSV]

    def setfilename(self, filename):
        self.__file_name = filename

    def getfilename(self):
        return self.__file_name

    file_name = property(getfilename, setfilename)

    def setnameWindow(self, nameWindow):
        self.__nameWindow = nameWindow

    def getnameWindow(self):
        return self.__nameWindow

    nameWindow = property(getnameWindow, setnameWindow)

    def setimg(self, img):
        self.__img = img

    def getimg(self):
        return self.__img

    img = property(getimg, setimg)

    def colors(self, event, x, y, flags, param):
        global ix, iy, jx, jy, c, color
        if event == cv2.EVENT_RBUTTONDOWN:
            color = random.choice(self.list)
            c = True
        elif event == cv2.EVENT_RBUTTONUP:
            jx, jy = x, y
            c = False
            self.img = cv2.cvtColor(self.img, color)
            cv2.imshow(self.nameWindow, self.img)

    def addText(self, event, x, y, flags, param):
        global xx, yy
        if event == cv2.EVENT_LBUTTONDOWN:
            xx, yy = x, y

    def draw_rect(self, event, x, y, flags, param):
        global ix, iy, jx, jy
        if event == cv2.EVENT_LBUTTONDOWN:
            ix = x
            iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            jx = x
            jy = y
            cv2.rectangle(self.img, (ix, iy), (jx, jy), (50, 50, 50), 3)
            cv2.imshow(self.nameWindow, self.img)
    def draw_rect1(self, event, x, y, flags, param):
        global ix, iy, jx, jy
        if event == cv2.EVENT_LBUTTONDOWN:
            ix = x
            iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            jx = x
            jy = y
            cv2.circle(self.img,(ix,iy),30,(50, 50, 50),-1)
            cv2.imshow(self.nameWindow, self.img)
    def cutImage1(self, event, x, y, flags, param):
        global ix, iy, jx, jy, c
        if event == cv2.EVENT_LBUTTONDOWN:
            ix, iy, jx, jy = x, y, x, y
            c = True
        elif event == cv2.EVENT_LBUTTONUP:
            jx, jy = x, y
            c = False
            imgcut = self.img[ix:jx, iy:jy]
            cv2.imshow("Cropped", imgcut)

    def cheeseImage(self, event):
        self.file_name = askopenfilename(initialdir="C:\\image", title="cheeseImage")
        self.nameWindow = "image"
        self.img = cv2.imread(self.file_name)
        self.img = cv2.resize(self.img, (800, 600))
        cv2.imshow(self.nameWindow, self.img)

    def Shades(self, event):
        cv2.setMouseCallback(self.nameWindow, self.colors)

    def cutImage(self, event):
        cv2.setMouseCallback(self.nameWindow, self.cutImage1)

    def drawsquare(self, event):
        cv2.setMouseCallback(self.nameWindow, self.draw_rect)
        cv2.imshow(self.nameWindow, self.img)
    def drawsC(self, event):
        cv2.setMouseCallback(self.nameWindow, self.draw_rect1)
        cv2.imshow(self.nameWindow, self.img)
    def blurImage(self, event):
        self.img = cv2.GaussianBlur(self.img, (3, 3), 0)
        cv2.imshow(self.nameWindow, self.img)

    def color(self, event):
        self.img = cv2.cvtColor(self.img, cv2.AKAZE_DESCRIPTOR_MLDB_UPRIGHT)
        cv2.imshow(self.nameWindow, self.img)

    def text(self, text):
        global xx, yy
        cv2.setMouseCallback(self.nameWindow, self.addText)
        cv2.putText(self.img, str(text.get()), (xx, yy), cv2.FONT_HERSHEY_PLAIN, 3.5, (50, 50, 50), 4)
        cv2.imshow(self.nameWindow, self.img)

    def blackwrite(self, event):
        self.img = cv2.Canny(self.img, 200, 300)
        cv2.imshow(self.nameWindow, self.img)

    def save(self, text):
        cv2.imwrite(text + ".jpg", self.img)
        messagebox.showinfo('Message', 'The image has been saved as:'+text)
