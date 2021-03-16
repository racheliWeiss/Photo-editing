from tkinter import *

import cv2
import myimage


def close(self):
    x.quit()


class window:
    def __init__(self, win):
        self.img = myimage.myimage(win)
        self.t1 = Entry(win)
        self.t2 = Entry(win)
        self.btn1 = Button(win, text='בחירת תמונה', bd="2", font=('calibri', 20, 'bold', 'underline'),
                           foreground='pink')
        self.btn2 = Button(win, text='        חיתוך תמונה       ', bd="4", bg="grey")
        self.btn3 = Button(win, text='ציור ריבוע על התמונה', bd="4", bg="grey")
        self.btn4 = Button(win, text='הוספת טקסט לתמונה', bd="4", bg="grey", command=lambda: self.img.text(self.t1))
        self.btn5 = Button(win, text='     טשטוש תמונה    ', bd="4", bg="grey")
        self.btn6 = Button(win, text=' שינוי גוונים לתמונה', bd="4", bg="grey")
        self.btn7 = Button(win, text='  תמונה בשחור לבן  ', bd="4", bg="grey")
        self.btn8 = Button(win, text='      שמירת תמונה     ', bd="4", bg="grey",
                           command=lambda: self.img.save(self.t2.get()))
        self.btn9 = Button(win, text='             יציאה            ', bd="4", bg="grey")
        self.btn10 = Button(win, text='הוספת עיגול לתמונה', bd="4", bg="grey")
        self.lbl1 = Label(win, text='הכנס טקסט:')
        self.lbl2 = Label(win, text='שם לתמונה:')
        self.positions()
        self.events()

    def positions(self):
        self.btn1.place(x=170, y=50)
        self.btn2.place(x=20, y=150)
        self.btn3.place(x=20, y=200)
        self.btn4.place(x=20, y=250)
        self.btn5.place(x=200, y=200)
        self.btn6.place(x=200, y=150)
        self.btn7.place(x=350, y=150)
        self.btn8.place(x=200, y=250)
        self.btn9.place(x=350, y=250)
        self.btn10.place(x=350, y=200)
        self.lbl1.place(x=20, y=300)
        self.lbl2.place(x=200, y=300)
        self.t1.place(x=20, y=320)
        self.t2.place(x=200, y=320)

    def events(self):
        self.btn1.bind('<Button-1>', self.img.cheeseImage)
        self.btn2.bind('<Button-1>', self.img.cutImage)
        self.btn3.bind('<Button-1>', self.img.drawsquare)
        self.btn5.bind('<Button-1>', self.img.blurImage)
        self.btn6.bind('<Button-1>', self.img.color)
        self.btn7.bind('<Button-1>', self.img.blackwrite)
        self.btn9.bind('<Button-1>', close)
        self.btn10.bind('<Button-1>', self.img.drawsC)


x = Tk()
mywin = window(x)
x.title("ProjectImage")
x.geometry("500x400+90+100")
x.mainloop()
