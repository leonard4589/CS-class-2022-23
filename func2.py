import numpy as np
import matplotlib.plyplot as plt 


def slope(x1, y1, x2, y2):
    try:
        s = (y2 - y1)/(x2 - x1)
    except:
        s = None
    return s 

def yintercept(x1, x2, y1, y2):
    try:
        yintercept = -(slope(x1,y1,x2,y2)*x1) + y1 
    except:
        yintercept = None
    return yintercept 

def graph(x1, x2, y1, y2):
    y = slope(x1, x2, y1, y2)*x1 + yintercept(x1, x2, y1, y2)
    return y 

x1 = 2
y1 = 5
x2 = 2
y2 = 10

x = []
y = []

for i in range(-10,10):
    x.append(i)
    y.append(f(i))

print("Slope = ", slope(x1,y1,x2,y2))

print("y-intercept = ", yintercept(x1,x2,y1,y2))

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()
