import pyqrcode
import png

qr = pyqrcode.create ('Sonu how are you...i hope you doing well')
qr.png('barc.png',scale=7)

print ("Barcode is Generating...!!!!!!")
