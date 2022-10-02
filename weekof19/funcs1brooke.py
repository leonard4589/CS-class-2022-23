import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

class picoLED:
    def __init__(self, nPix=20):
        self.nPix = nPix

    def LightsB(self):
        for i in range(20):
            pixels[i] = (0, 0, 10)
            time.sleep(0.1)
   