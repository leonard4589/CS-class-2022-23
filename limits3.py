import matplotlib.pyplot as plt 
import numpy as np

def misval(x):
    dx = 0.0000001
    try:
        y = (x**3 + 125)/(x + 5)
    except:
        y = (misval(x+dx) + misval(x-dx)) / 2
    return y 

def lim(x):
    y = x
    return y 

x = 5

xa = []
ya = []

for i in range(-5, 5):
    ya.append (misval(i))
    xa.append ((i))
    print(i, misval(i))

print (xa, ya)
   

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()



