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
        self.title("Face Cropper")
        self.minsize(640, 400)

        name=Label(text='Real Time Theft Detection Using Facial Recoginition', font=("Times new Roman",15),relief='ridge', bg='cadet blue', bd=6).place(x=90, y=10, width=500, height=40)
        module=Label(text='Face Cropper', font=("Times new Roman",18), bg="Orange").place(x=130, y=100, width=400, height=40)

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


        # Load some pre-trained data on face frontal from opencv (haar cascade algorithm)
        trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Choose an image to detect faces in
        img = cv2.imread(self.filename)

        # Must convert to greyscale
        grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect Faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

        img_crop = []

        # Draw rectangles around the faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img_crop.append(img[y:y + h, x:x + w])

        for counter, cropped in enumerate(img_crop):
            cv2.imshow('Cropped', cropped)
            cv2.imwrite("pose_result_{}.png".format(counter), cropped)
            cv2.waitKey(0)

root = Root()
root.mainloop()

    