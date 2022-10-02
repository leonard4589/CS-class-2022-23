import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

n1 = 0
n2 = 1

while (n2 < 20):
    pixels[n2] = (0,10,10)
    n2old = n2
    n2 = n2 + n1
    n1 = n2old