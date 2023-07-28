import qrcode

data = "Meow Cat's actually meaningless QR code lol"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)

image = qr.make_image(fill_color = "red", back_color = "white")

image.save("H:/Mandy/my_QR_code_2.png")