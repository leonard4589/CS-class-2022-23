import numpy as np
import matplotlib.pyplot as plt

#12. Write a program that takes two given x values (x = 2 and x = 3), finds the corresponding y values for the equation y=1/x and then finds the slope of the line between the two points. Graph the two lines.
def Y(x):
    try:
        y = 1/x
    except:
        y = None
    return y 

def slope(x1, y1, x2, y2):
    try:
        s = (y2 - y1)/(x2 - x1)
    except:
        s = None
    return s

def graph(x1, x2, y1, y2):
    y = slope(x1, x2, y1, y2)*x1 + yintercept(x1, x2, y1, y2)
    return y

def yintercept(x1, x2, y1, y2):
    try:
        yintercept = -(slope(x1,y1,x2,y2)*x1) + y1 
    except:
        yintercept = None
    return yintercept 

x1 = 2
x2 = 3

y1 = Y(x1)
y2 = Y(x2)

x = []
y = []
ya = []

m = slope(x1,y1,x2,y2)
b = yintercept(x1,x2,y1,y2)

for i in range(-10,11):
    x.append(i)
    y.append(m*i+b)
    ya.append(Y(i))
print(x)
print(y)
print(ya)

print(slope(x1,y1,x2,y2))

fig, ax = plt.subplots()
ax.plot(x, y, ya)

plt.show()