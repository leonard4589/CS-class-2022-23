import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

def steps():
    i = 19   
    while (i > 10):   
      pixels[i] = (0,10,0)
      i = i - 1
      time.sleep(0.1)
  