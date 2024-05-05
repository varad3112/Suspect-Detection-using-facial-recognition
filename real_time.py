import cv2
from simple_facerec import SimpleFacerec
from email import message
from email.quoprimime import body_check
import smtplib as s

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("img/known/")

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

        ob = s.SMTP("smtp.gmail.com",587)

        ob.starttls()

        ob.login("theftdetection1234@gmail.com","Theft1234")

        subject = "Sending Message using Python"
        #body = "Hello, this is varad,manish,aftab,pratik,karan are the members of project"
        body = "Hello "+name+" detected"

        message = "Subject:{}\n\n{}".format(subject,body)

        # print(message)

        listOfAddress = ["varadkulkarni3112@gmail.com","pratikghorpade11aug@gmail.com"]

        ob.sendmail("theftdetection1234",listOfAddress,message)

        print("Message Sent Successfully")
        ob.quit()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()