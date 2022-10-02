import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

def example():
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
def ass1():
    for i in range(20):
        if (i <= 8):
            pixels[i] = (0, 0, 10)
        else:
            pixels[i] = (10, 0, 0)
# assignment #2
def ass2():
    for i in range(20):
        if (i > 8):
            pixels[i] = (10, 0, 0)
        else:
            pixels[i] = (0, 0, 10)
# assignment #3
def ass3():
    for i in range(20):
        if (i >= 9):
            pixels[i] = (10, 0, 0)
        else:
            pixels[i] = (0, 0, 10)
# assignment #4
def ass4():
    for i in range(20):
        if (i != 2):
            pixels[i] = (0, 10, 0)
        else:
            pixels[i] = (10, 0, 0)
def example2():        
    for i in range(20):
        if (i%3) == 0:
            pixels[i] = (0, 40, 0)

# assignment #5
def ass5():
    for i in range(20):
        if (i%3) != 0:
            pixels[i] = (0, 0, 10)
# assignment #6
def ass6():
    for i in range(20):
        if (i%5) == 0:
            pixels[i] = (0, 10, 0)
            time.sleep (1)
        else:
            pixels[i] = (0, 10, 0)
            time.sleep(0.1)

def example3():
    for i in range(20):
        if not(((i%2) == 0) and ((i%3) == 0)):
            pixels[i] = (0,10,0)

# assignment #7
def ass7():
    for i in range(20):
        if ((i>10) and ((i%2) == 0)):
            pixels[i] = (0, 10, 0)
        else:
            pixels[i] = (10, 0, 0)
# assignment #8
def ass8():
    for i in range(20):
        if (((i%3) == 0) and ((i%4) == 0)):
            pixels[i] = (0, 10, 0)
        else:
            pixels[i] = (10, 0, 0)
# assignment #9
def ass9():
    for i in range(20):
        if not (((i%3) == 0) and ((i%4) == 0)):
            pixels[i] = (0, 10, 0)
        else:
            pixels[i] = (10, 0, 0)
# assignment #20
def ass20():
    for i in range(20):
        for n in range(20):
            if n != i:
                pixels[n] = (0, 40, 0)
            else:
                pixels[n] = (40, 0, 0)
        time.sleep(0.1)
        
