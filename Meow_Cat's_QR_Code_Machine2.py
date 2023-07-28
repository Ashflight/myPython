from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open("H:/Mandy/my_QR_code.png")

result = decode(image)

print(result)