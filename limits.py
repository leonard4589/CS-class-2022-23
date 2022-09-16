from asyncio import as_completed
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = (x**2 - 2*x)/(x - 2)
    return y 

x = []
y = []

for i in range(-5, 5):
    x.append (i)
    y.append (f(i))
    print(x[-1], y[-1])

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()