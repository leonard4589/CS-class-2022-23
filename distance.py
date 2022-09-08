from tkinter import Y
from vpython import *
#calculate the distance between two points given two "x" values and a function

#function
def f1(x):
    y = 2*x +3
    return y

#inputs
x_1 = 1
x_2 = 5

#function
y_1 = f1(x_1)
y_2 = f1(x_2)

#calculate the change
dx = x_2 - x_1
dy = y_2 - y_1

#caluclate the distance using distance equation
distance = (dx**2 + dy**2)**0.5

#calculate the slope equation
slope = dy/dx

print ("Distance =", distance)
print ("Slope =", slope)

#same thing with a quadratic equation instead
def f2(x):
    y = 2*x**2 + 3*x + 4
    return y

x1 = 1
x2 = 5

y1 = f2(x1)
y2 = f2(x2)

dX = x2 - x1
dY = y2 - y1

d = (dX**2 + dY**2)**0.5

print ("Distance of a quad funtion =", d)
