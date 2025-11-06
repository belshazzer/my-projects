import pyqrcode 
import png

data = input("Enter text or link to generate QR code: ")
filename = input("Enter the filename to save the QR code (without .png): ")

qr = pyqrcode.create(data)

qr.png(f"{filename}.png", scale=8)

print(f"QR code saved succesfully as {filename}.png")
