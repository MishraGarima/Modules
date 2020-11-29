#Python Code for Sending a Mail with Image Attachment

#importing required packages
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#define a function/method to send mail with an image attachment
def SendMail(ImgFileName):
	#open the image file in read mode
	img_data = open(ImgFileName, 'rb').read()
	#create a mail object
	msg = MIMEMultipart()
	#specifying mail headers
    msg['Subject'] = 'Subject'
    msg['From'] = 'sender@gmail.com'
    msg['To'] = 'receiver@gmail.com'

	#specifying mail body
    text = MIMEText("This is the mail using python code")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    Server='smtp.gmail.com'
    Port='587'
    UserName='sender@gmail.com'
	#enter password for the email used
    UserPassword=' '
    From='sender@gmail.com'
    To='receiver@gmail.com'

	#Sending mail works as mentioned :
	#start the server, login in the sender email, send mail, and finally quit/stop the server
    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(UserName, UserPassword)
    s.sendmail(From, To, msg.as_string())
    s.quit()

#Enter image name directly to be sent if the image file is in same folder else, enter path as well
img="data.jpeg"
SendMail(img)
#print("done")
