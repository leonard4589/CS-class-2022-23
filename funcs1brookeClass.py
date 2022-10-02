import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

class picoLED:
    def __init__(self, nPix=20):
        self.nPix = nPix

    def LightsG(self):
        for i in range(20):
            pixels[i] = (0, 10, 0)
            time.sleep(0.1)

    def LightsOff(self):
        for i in range(20):
            pixels[i] = (0,0,0)
            time.sleep(0.1)
            
    def LightsR(self):
        for i in range(20):
            pixels[i] = (10, 0, 0)
            time.sleep(0.1)
            
    def LightsB(self):
        for i in range(20):
            pixels[i] = (0, 0, 10)
            time.sleep(0.1)
    # assignment #3        
    def lightSequence(self, color):
        for i in range(20):
            pixels[i] = color
            time.sleep(0.1)
    # assignment #4:
    def backwards(self, color):
        i = 19
        while (i > -1):
            pixels[i] = color
            i = i - 1
            time.sleep(0.1)
            
    def lightRGB(self, a, b, c):
        pixels[a] = (10, 0, 0)
        pixels[b] = (0, 10, 0)
        pixels[c] = (0, 0, 10)
    # assignment #5/#7
    def LightUp(self, a = 20, color = (0, 0, 10)):
        for i in range(a):
            pixels[i] = color
            time.sleep(0.1)
    # assignment #6
    #lightRGB(1, 2, 3, 4)
    # error message: function takes 3 positional arguments but 4 were given
    # assignment #8
    def lastLights(self, n = 20, color = (0, 10, 0)):
        x = 20 - n
        for i in range (x, 20, 1):
            pixels[i] = color
            time.sleep(0.1)
    # assignment #9
    def stepLights(self, step = 1, color = (0, 10, 0)):
        for i in range(20):
            pixels[i] = color
            time.sleep(0.1)

    def complementaryColor(self, color):
        r = 255 - color[0]
        g = 255 - color[1]
        b = 255 - color[2]
        return (r, g, b)
    # the following is running complementaryColor:
    # color1 = (0, 0, 255)
    # compColor = complementaryColor(color1)
    # print(compColor)
    # 
    # pixels[0] = color1
    # pixels[-1] = compColor
    # assignment #10
    def scalingCompColors(self, color, scaleValue):
        r = scaleValue - color[0]
        g = scaleValue - color[1]
        b = scaleValue - color[2]
        return (r, g, b)
    # the following is running scalingCompColors:
    # color1 = (7, 2, 10)
    # compColor = scalingCompColors(color1, 10)
    # for i in range(10):
    #     pixels[i] = color1
    #     pixels[i+10] = compColor
    
    def upDown(self):
        self.LightUp()
        self.LightsOff()
        
    def example(self):
    for i in range(10):
        if (i != 4):
            pixels[i] = (0, 10, 0)
        else:
            pixels[i] = (10, 0, 0)
        
 "==" = equal to
 "!=" = not equal to
 "<" = less than
 ">" = greater than
 "<=" = less than or equal to
 ">=" = greater than or equal to
    #  assignment #1
    def ass1(self):
        for i in range(20):
            if (i <= 8):
                pixels[i] = (0, 0, 10)
            else:
                pixels[i] = (10, 0, 0)
    # assignment #2
    def ass2(self):
        for i in range(20):
            if (i > 8):
                pixels[i] = (10, 0, 0)
            else:
                pixels[i] = (0, 0, 10)
    # assignment #3
    def ass3(self):
        for i in range(20):
            if (i >= 9):
                pixels[i] = (10, 0, 0)
            else:
                pixels[i] = (0, 0, 10)
    # assignment #4
    def ass4(self):
        for i in range(20):
            if (i != 2):
                pixels[i] = (0, 10, 0)
            else:
                pixels[i] = (10, 0, 0)
    def example2(self):        
        for i in range(20):
            if (i%3) == 0:
                pixels[i] = (0, 40, 0)

    # assignment #5
    def ass5(self):
        for i in range(20):
            if (i%3) != 0:
                pixels[i] = (0, 0, 10)
    # assignment #6
    def ass6(self):
        for i in range(20):
            if (i%5) == 0:
                pixels[i] = (0, 10, 0)
                time.sleep (1)
            else:
                pixels[i] = (0, 10, 0)
                time.sleep(0.1)

    def example3(self):
        for i in range(20):
            if not(((i%2) == 0) and ((i%3) == 0)):
                pixels[i] = (0,10,0)

    # assignment #7
    def ass7(self):
        for i in range(20):
            if ((i>10) and ((i%2) == 0)):
                pixels[i] = (0, 10, 0)
            else:
                pixels[i] = (10, 0, 0)
    # assignment #8
    def ass8(self):
        for i in range(20):
            if (((i%3) == 0) and ((i%4) == 0)):
                pixels[i] = (0, 10, 0)
            else:
                pixels[i] = (10, 0, 0)
    # assignment #9
    def ass9(self):
        for i in range(20):
            if not (((i%3) == 0) and ((i%4) == 0)):
                pixels[i] = (0, 10, 0)
            else:
                pixels[i] = (10, 0, 0)
    # assignment #20
    def ass20(self):
        for i in range(20):
            for n in range(20):
                if n != i:
                    pixels[n] = (0, 40, 0)
                else:
                    pixels[n] = (40, 0, 0)
            time.sleep(0.1)

    
    
        
        

        



        
         
    
    


