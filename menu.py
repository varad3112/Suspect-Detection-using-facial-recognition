import builtins
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
#from open import click
#from Pull_Faces import *


class login:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        # Bg Image
        self.bg=ImageTk.PhotoImage(file="face1.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150, y=150, height=340, width=500)

        header = Label(text="Real Time Theft Detection Using Faial Recoginition", font=("Goudy old style",28), fg="black", bg="orange").place(x=220, y=30)


        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=90, y=30)
        desc = Label(Frame_login, text="Detector Security Login area", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white").place(x=90, y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="black",bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_btn = Button(Frame_login, text="Forget Password ?",cursor="hand2", bg="white", fg="#d77337", bd=0, font=("times new roman", 12)).place(x=90, y=280)
        login_btn = Button(self.root,command=self.Login_function,cursor="hand2", text="Login", fg="white", bg="orange", font=("times new roman", 20)).place(x=300, y=470, width=180, height=40)

    def Login_function(self):
       if (self.txt_user.get()=="" or self.txt_pass==""):
           messagebox.showerror("Error", "All fields are required", parent=self.root)
       elif (self.txt_user.get()== "admin" and self.txt_pass.get() == "admin"):
           messagebox.showinfo("Done", "Welcome! You are Logged in Successfully!", parent=self.root)
          
           menu_root = Tk()
           menu_root.geometry("1000x1000")
            #root.bg=ImageTk.PhotoImage(file="fg.jpg")
           Label(menu_root, text="Menu Page", font="arial 30 bold", bg="red").place(x=230, y=30, width=420, height=60)
            

           count_btn = Button(menu_root, text="Face Counter", font="Impact 15", bg="skyblue").place(x=50, y=100, width=250, height=40)
           cut_btn = Button(menu_root, text="Face Cutter", font="Impact 15", bg="skyblue" ).place(x=550, y=100, width=250, height=40)
           face_btn = Button(menu_root, text="Face Recognizer", font="Impact 15", bg="skyblue").place(x=50, y=180, width=250, height=40)
           r_face_btn = Button(menu_root, text="Real TIme Face Recognizer", font="Impact 15", bg="skyblue").place(x=550, y=180, width=250, height=40)
           log_btn = Button(menu_root, text="LOG OUT", font="Impact 15", bg="Yellow").place(x=330, y=250, width=180, height=40)
           
           self.root.destroy()
           menu_root.mainloop() 
       
       else:
           messagebox.showerror("Error", "Invalid Username or Password")
           
           

           
            


    
   

          

          

           
          


root = Tk()
obj = login(root)
root.mainloop()
         

                        


               





