import qrcode

img = qrcode.make("https://youtu.be/CRheG1Nb0w0")
img.save("qr.png", "PNG")