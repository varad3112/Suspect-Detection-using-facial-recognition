import face_recognition
from time import sleep
from tkinter import messagebox
 
img_of_bill = face_recognition.load_image_file('./img/known/Robert Downey Jr..jpg')
bill_face_encoding = face_recognition.face_encodings(img_of_bill)[0]

unknown_img = face_recognition.load_image_file('./img/unknown/iron.jpg')
unknown_face_encodings = face_recognition.face_encodings(unknown_img)[0]

    # Compare Faces
results = face_recognition.compare_faces([bill_face_encoding], unknown_face_encodings)

if results[0]:
    messagebox.showinfo("Attention", 'Both are same Persons')
else:
    messagebox.showinfo("Attention", 'Both are Different Persons')



