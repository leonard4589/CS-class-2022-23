import numpy as np
import matplotlib.pyplot as plt 
#Write a function that is passed the x,y coordinates of two points and returns the slope of the line between them. (If the slope is undefined, it should return None).
#Write a function that is passed the x,y coordinates of two points and returns the y-intercept of the straight line that connects the two points.
#Write a function that graphs a straight line between [-10,10] if given the slope and the intercept of the line.


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
x2 = 4
y2 = 10

x = []
y = []

m = slope(x1,y1,x2,y2)
b = yintercept(x1,x2,y1,y2)

for i in range(-10,11):
    x.append(i)
    y.append(m*i+b)

print("Slope = ", slope(x1,y1,x2,y2))

print("y-intercept = ", yintercept(x1,x2,y1,y2))

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()
