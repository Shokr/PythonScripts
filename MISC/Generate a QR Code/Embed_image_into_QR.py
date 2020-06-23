# Embed the image into the QR code

import qrcode
from PIL import Image

faceX = Image.open("shokr.jpg")

# Provide the target width and height of the image
(width, height) = (faceX.width // 30, faceX.height // 30)

face = faceX.resize((width, height))

qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data('I am Muhammed Shokr')
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')

pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('qr_shokr.png')