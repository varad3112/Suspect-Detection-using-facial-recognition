from time import sleep
from tkinter import *
from tkinter import ttk
import random
from tkinter import font
from click import command
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
import turtle

def click():

    class Root(Tk):
     def __init__(self):
         super(Root, self).__init__()
         self.title("Face Cropper")
         self.minsize(700, 400)

         self.labelFrame = ttk.LabelFrame(self, text = "Open File")
         #self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
         self.labelFrame.place(x=200, y=150)

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
                messagebox.showwarning("Alert !", "The Theft has been Caught")
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
    


######################################### Face Cutter #######################################################
def crop():
    class Root(Tk):
     def __init__(self):
         super(Root, self).__init__()
         self.title("Face Cropper")
         self.minsize(700, 400)

         self.labelFrame = ttk.LabelFrame(self, text = "Open File")
         #self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
         self.labelFrame.place(x=200, y=150)

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
        


############################################## Face Counter #################################################
def count():   
    class Root(Tk):
     def __init__(self):
        super(Root, self).__init__()
        self.title("Face Counter")
        self.minsize(700, 400)

        self.labelFrame = ttk.LabelFrame(self, text = "Face Counter")
        #self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.labelFrame.place(x=200, y=150)
        #self.labelFrame.config(bg="cadet blue")

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

        messagebox.showinfo("Done",f'There are {len(face_locations)} peoples in this image')
    root = Root()
    root.mainloop()


######################################### Simple Comparison Tool ###############################################
def compare() :
    img_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
    bill_face_encoding = face_recognition.face_encodings(img_of_bill)[0]

    unknown_img = face_recognition.load_image_file('./img/unknown/bill-gates-4.jpg')
    unknown_face_encodings = face_recognition.face_encodings(unknown_img)[0]

    # Compare Faces
    results = face_recognition.compare_faces([bill_face_encoding], unknown_face_encodings)

    if results[0]:
        messagebox.showinfo("Attention", 'Both are same Persons')
    else:
        messagebox.showinfo("Attention", 'Both are Different Persons')


######################################### Rael Time Theft Detection ###############################################
def real():
    import cv2
    from simple_facerec import SimpleFacerec

    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("img/known/")

    messagebox.showinfo("Attention", 'Please wait a minute, We are processing')

    # Load Camera
    cap = cv2.VideoCapture(0)


    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (248,248,255), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (248,248,255), 4)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if(key == 27):
            break

    cap.release()
    cv2.destroyAllWindows()


######################################### Age and Gender Detector ###############################################



    
    

#################################################### Login Page ##################################################

class login:

    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

    
        # Bg Image
        self.bg=ImageTk.PhotoImage(file="fg.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        Frame_login = LabelFrame(self.root, width=800, height=400,font=("arial", 20, "bold"), relief='ridge', bg='cadet blue', bd=20)
        Frame_login.place(x=210, y=150)

        

        header = Label(text="Real Time Theft Detection Using Facial Recoginition", font=("Goudy old style",28), fg="black", bg="orange").place(x=220, y=30)
        
        title = Label(Frame_login, text="Security Login Page", font=("Goudy old style", 35, "bold"), fg="black", bg="cadet blue").place(x=220, y=30)
       # desc = Label(Frame_login, text="Detector Security Login area", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white").place(x=90, y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 20, "bold"), fg="black", bg="cadet blue", bd=22).place(x=90, y=120)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=240, y=140, width=350, height=32)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 20, "bold"), fg="black",bg="cadet blue", bd=22).place(x=90, y=190)
        self.txt_pass = Entry(Frame_login, font=("arial", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=240, y=210, width=350, height=32)

        #forget_btn = Button(Frame_login, text="Forget Password ?", cursor="hand2", bg="white", fg="#d77337", bd=0, font=("times new roman", 12)).place(x=90, y=280)
        login_btn = Button(self.root,command=self.Login_function,cursor="hand2", text="Login", fg="white", bg="orange", font=("times new roman", 20)).place(x=400, y=470, width=180, height=40)
       # rest_btn = Button(self.root,cursor="hand2",command=self.iReset, text="Reset", fg="white", bg="orange", font=("times new roman", 20)).place(x=540, y=470, width=180, height=40)
        exit_btn = Button(self.root,command=self.iExit,cursor="hand2", text="Exit", fg="white", bg="orange", font=("times new roman", 20)).place(x=700, y=470, width=180, height=40)
    
           

    def iExit(self) :
        self.iExit = messagebox.askyesno("Login System", "Are you sure, you want to exit ?")
        if self.iExit > 0 :
            self.root.destroy()
        else:
            COMMAND = self.root
            return

    def logout(self):
        self.logout = messagebox.askyesno("Menu Page", "Are you sure, you want to Logout ?")
        if self.logout > 0 :
            self.menu_root.destroy()
        else:
            COMMAND=self.root
            return
             


    def Login_function(self):
       if (self.txt_user.get()=="" or self.txt_pass==""):
           messagebox.showerror("Error", "All fields are required", parent=self.root)
       elif (self.txt_user.get()== "admin" and self.txt_pass.get() == "admin"):
           messagebox.showinfo("Done", "Welcome! You are Logged in Successfully!", parent=self.root)
          
          
          # Menu Page
           self.menu_root = Tk()
           self.menu_root.title("Real Time Theft Detection Using Facial Recoginition")
           self.menu_root.geometry("1600x800+100+50")
           self.menu_root.config(bg="cadet blue")
           
           '''# Bg Image
           self.menu_root.bg=ImageTk.PhotoImage(file="face.jpeg")
           self.menu_root.bg_image=Label(self.menu_root, image=self.menu_root.bg).place(x=0, y=0, relwidth=1, relheight=1)
           '''
           
           Frame_menu = Label(self.menu_root, text="Menu Page", font=("Impact", 20), relief='ridge', bg='cadet blue', bd=16).place(x=500, y=30, width=420, height=60)
            

           count_btn = Button(self.menu_root, text="Face Counter", font="Impact 15", bg="skyblue", command=count).place(x=280, y=140, width=250, height=40)
           cut_btn = Button(self.menu_root, text="Face Cutter", font="Impact 15", bg="skyblue", command=crop ).place(x=600, y=140, width=250, height=40)
           camp_btn = Button(self.menu_root, text="Simple Comparison Tool", font="Impact 15", bg="skyblue", command=compare).place(x=950, y=140, width=250, height=40) 
       
           face_btn = Button(self.menu_root, text="Face Recognizer", font="Impact 15", bg="skyblue", command=click).place(x=280, y=400, width=250, height=40)
           r_face_btn = Button(self.menu_root, text="Real TIme Face Recognizer", font="Impact 15", bg="skyblue", command=real).place(x=600, y=400, width=250, height=40)
           age_btn = Button(self.menu_root, text="Age & Gender Detetor", font="Impact 15", bg="skyblue").place(x=950, y=400, width=250, height=40) 
                   
           logout_btn = Button(self.menu_root,command=self.logout, text="LOG OUT",  font="Impact 15", bg="red").place(x=620, y=700, width=180, height=40)

           counter_label = Label(self.menu_root, text="This is Face Counter Tool. \nThis Module will accept an image from user,\n and then after processing it will detect there\n are total how many faces in the provided\n image and display you the count.", font=("Times new Roman", 12), bg="yellow").place(x=250, y=190, width=300, height=200)
           cutter_label = Label(self.menu_root, text="This is a simple Face Cutter Tool . \nWhich is a Simple part of our Project\n This Module will take image as a input from\n Operator. After receiving image it will start \nprocessing means start detecting face locations in \nimage.And after detection it crop exact faces \nfrom the image and will store it into the database", font=("Times new Roman", 12), bg="orange").place(x=570, y=190, width=300, height=200)
           camp_label = Label(self.menu_root, text="This is a Simple Comparison Tool.\nJust Give locations of Images that you\n want to compare and press the \nbutton it will compare the images and show the message", font=("Times new Roman", 12), bg="yellow").place(x=920, y=190, width=300, height=200)

           face_label = Label(self.menu_root, text="Face Detection Using Database .\nThis is another module in our system.\nThis is face recognizer that will process on\n database. This system will receive test image \nfrom operator that it want to be recognize.\nThen this system will start processing.", font=("Times new Roman", 12), bg="orange").place(x=250, y=450, width=300, height=200)
           r_face_label = Label(self.menu_root, text=" This is main and important part of our system.\nAs name suggest it is a real time theft detector.\n After starting this module it will first access\n the webCam or attached camera of the respective \nsystem.And it will start capturing faces", font=("Times new Roman", 12), bg="yellow").place(x=570, y=450, width=300, height=200)
           age_label = Label(self.menu_root, text="This is another module which is also real time \ndetector. As name suggest it will capture images \nfrom the web camera and start processing on\nthe face features and face encodings of the\nperson Infront of the camera & it will \ndisplay the Gender of that person and \nalso using these features it will predict the age \nof that person ", font=("Times new Roman", 12), bg="orange").place(x=920, y=450, width=300, height=200)

           logo_label = Label(self.menu_root, text="---Real Time Theft Detection Using Facial Recoginition",font=("Times new Roman", 12),bg="cadet blue", fg="Black").place(x=1000, y=730, width=700, height=100)

           self.root.destroy()
           self.menu_root.mainloop() 
       
       else:
           messagebox.showerror("Error", "Invalid Username or Password")

    

    
            
        


root = Tk()
obj = login(root)
root.mainloop()











