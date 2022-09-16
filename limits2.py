import numpy as np
import matplotlib.plyplot as plt

#f(x) = (x**2 - 2*x)/(x - 2)

def misval(x):
    try:
        y = (x**2 - 2*x)/(x - 2)
    except:
        y = (misval(x+dx) + misval(x-dx)) / 2
    return y 

def lim(x):
    y = x
    return y 

x = 2
dx = 0.00000000001

x = []
y = []

for i in range(-5, 5):
    x.append (i)
    y.append (f(i))
   

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()





#print(misval(x)) 

# try:
#     print(misval(x))
# except:
#     #print("No value. Limit is: ", lim(x))
#     y = (misval(x+dx) + misval(x-dx)) / 2
#     print(y)

print(misval(x))
