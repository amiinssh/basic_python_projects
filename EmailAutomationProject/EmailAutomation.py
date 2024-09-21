import smtplib

to = input("Enter the reciever's email address: ")
message = input("Enter the message: ")

def sendMail(to, message):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("senderemail", "password")
    server.sendmail("senderemail", to, message)
    server.close()


sendMail(to, message)
