import board
import neopixel

pixels = neopixel.NeoPixel(board.GP0, 20)

def skip():
    i = 0   # initialize variable
    while (i < 20):   # loop with check
      pixels[i] = (0,10,0)
      i = i + 2 # increase the value of i
    