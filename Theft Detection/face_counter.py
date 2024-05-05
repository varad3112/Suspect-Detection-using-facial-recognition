from turtle import width
import face_recognition
from tkinter.constants import COMMAND
from PIL import Image
import  face_recognition
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Face Counter")
        self.minsize(700, 400)

        sname=Label(text='Real Time Theft Detection Using Facial Recoginition', font=("Times new Roman",15),relief='ridge', bg='cadet blue', bd=6).place(x=90, y=10, width=500, height=40)
        module=Label(text='Face Counter', font=("Times new Roman",18), bg="Orange").place(x=130, y=100, width=400, height=40)

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
         #self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.labelFrame.place(x=280, y=150)
        self.button()



    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
      



    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)

        image = face_recognition.load_image_file(self.filename)
        face_locations = face_recognition.face_locations(image)

        # Array of Co-ordinates of each face
        print(face_locations)

        print(f'There are {len(face_locations)} peoples in this image')

root = Root()
root.mainloop()
