import pyqrcode
import png
from pyqrcode import QRCode

s = input('Enter the subject to make the qrcode ')

url = pyqrcode.create(s)

url.svg('generate_qrcode.png',scale = 9)

url.png('generate_qrcode.png',scale=9)
