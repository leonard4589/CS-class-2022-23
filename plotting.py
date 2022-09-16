import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = ((x**2) - 2*x)/(x - 2)
    return y 

print (f(-5))

xa = []
ya = []


for i in np.arange(-5, 5):
    xa.append(i)
    ya.append(f(i))

fgi, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()