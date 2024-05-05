from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main () :
    root = Tk()
    app = window1(root)

class window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Real Time Theft Detection Using Faial Recoginition")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.btnLogin = Button(self.frame, text='Login', width=17, command=self.new_window)
        self.btnLogin.grid(row=3, column=0)

        self.btnReset = Button(self.frame, text='Reset', width=17)
        self.btnReset.grid(row=3, column=1)

        self.btnExit = Button(self.frame, text='Exit', width=17)
        self.btnExit.grid(row=3, column=2)


    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window2(self.newWindow)

class window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu Page")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='cadet blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

if main == 'main__' :
    main()

























