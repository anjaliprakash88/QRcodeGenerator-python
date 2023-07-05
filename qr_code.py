import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=8Y7bYQIWcuk&ab_channel=Charu%27sMusicWorld")
img.save("qr.png")