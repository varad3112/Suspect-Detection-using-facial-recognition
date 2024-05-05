from email import message
from email.quoprimime import body_check
import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("theftdetection1234@gmail.com","Theft1234")

subject = "Sending Message using Python"
body = "Hello, this is varad,manish,aftab,pratik,karan are the members of project"

message = "Subject:{}\n\n{}".format(subject,body)

#print(message)

listOfAddress =["varadkulkarni3112@gmail.com","pratikghorpade11aug@gmail.com"]

ob.sendmail("theftdetection1234",listOfAddress,message)

print("Message Sent Successfully")
ob.quit()
