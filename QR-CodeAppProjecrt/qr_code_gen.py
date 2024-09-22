import pyqrcode

url = input("Enter an URL to generate QR-Code: \n")

QR = pyqrcode.create(url)

QR.png("webqr.png", scale=8)