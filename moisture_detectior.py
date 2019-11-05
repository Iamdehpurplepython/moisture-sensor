from microbit import *


while True:
    moisture = pin0.read_analog()
    displayed = moisture // 40
    imgstr = ""
    for i in range(25):
        if i <= displayed:
            imgstr += "5"
        else:
            imgstr += "0"
        if (i + 1) % 5 == 0:
            imgstr += ":"
    image = Image(imgstr)
    display.show(image)