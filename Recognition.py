from time import sleep
from tkinter import *
from tkinter import ttk
import random
from tkinter import font
import face_recognition
from PIL import Image, ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import ImageTk
from tkinter import messagebox
from tkinter.constants import COMMAND
from PIL import Image
from tkinter import filedialog
import cv2
import numpy as np
import face_recognition
from PIL import Image, ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets

class Root(Tk):
     def __init__(self):
         super(Root, self).__init__()
         self.title("Face Detector")
         self.minsize(700, 400)
         
         name=Label(text='Real Time Theft Detection Using Facial Recoginition', font=("Times new Roman",15),relief='ridge', bg='cadet blue', bd=6).place(x=90, y=10, width=500, height=40)
         module=Label(text='Face Detector', font=("Times new Roman",18), bg="Orange").place(x=130, y=100, width=400, height=40)

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


        img_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
        bill_face_encoding = face_recognition.face_encodings(img_of_bill)[0]

        img_of_steve = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
        steve_face_encoding = face_recognition.face_encodings(img_of_steve)[0]

        image_of_elon = face_recognition.load_image_file('./img/known/Elon Musk.jpg')
        elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0]

        image_of_obama = face_recognition.load_image_file('./img/known/Barack Obama.jpg')
        obama_face_encoding = face_recognition.face_encodings(image_of_obama)[0]

        image_of_manish = face_recognition.load_image_file('./img/known/Manish.jpg')
        manish_face_encoding = face_recognition.face_encodings(image_of_manish)[0]

        image_of_donald = face_recognition.load_image_file('./img/known/Donald Trump.jpg')
        donald_face_encoding = face_recognition.face_encodings(image_of_donald)[0]

        image_of_michael = face_recognition.load_image_file('./img/known/Michael Jordan.jpg')
        michael_face_encoding = face_recognition.face_encodings(image_of_michael)[0]

        # Create array of encodings and names
        known_faces_encodings = [
            bill_face_encoding,
            steve_face_encoding,
            elon_face_encoding,
            obama_face_encoding,
            manish_face_encoding,
            donald_face_encoding,
            michael_face_encoding
        ]

        known_face_names = [
            "Bill Gates",
            "Steve Jobs",
            "Elon Musk",
            "Barack Obama",
            "Manish Barage",
            "Donald Trump",
            "Michael Jordan"
        ]

        # Load Face image to find faces in
        test_image = face_recognition.load_image_file(self.filename)
        # Find faces in test image
        face_locations = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image, face_locations)

        # Convert to PIL format
        pil_image = Image.fromarray(test_image)

        # Create ImageDraw instance
        draw = ImageDraw.Draw(pil_image)

        # Loop through faces in test image
        for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)

            name = "Unknown Person"

            # If match
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Draw Box
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

            # Draw Label
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

        del draw
        # Display image
        pil_image.show()
root = Root()
root.mainloop()


'''
if True in matches:
    class Ui_Dialog(object):
        def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(400, 150)
            Dialog.setMaximumSize(QtCore.QSize(400, 150))
            Dialog.setStyleSheet("background: rgb(255, 255, 255);")
            self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
            self.verticalLayout.setObjectName("verticalLayout")
            self.label_3 = QtWidgets.QLabel(Dialog)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Roboto")
            font.setPointSize(14)
            self.label_3.setFont(font)
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.label_3.setObjectName("label_3")
            self.verticalLayout.addWidget(self.label_3)
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setMinimumSize(QtCore.QSize(200, 0))
            self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
            self.pushButton.setStyleSheet("QPushButton{background:none;\n"
                                          " border:2px solid #4161AD;\n"
                                          " border-radius:6px;\n"
                                          " color:#4161AD;\n"
                                          " padding-top:5px;\n"
                                          " padding-bottom:5px;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(65, 97, 173);\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "}\n"
                                          "               \n"
                                          "               \n"
                                          "\n"
                                          "")
            self.pushButton.setObjectName("pushButton")
            self.horizontalLayout.addWidget(self.pushButton)
            self.verticalLayout.addLayout(self.horizontalLayout)

            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

        def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Alert !!"))
            self.label_3.setText(_translate("Dialog", "Theft has been Recognized !"))
            self.pushButton.setText(_translate("Dialog", "OK"))


    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
'''









