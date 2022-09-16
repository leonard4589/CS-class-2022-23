import matplotlib.pyplot as plt
from cmath import sin

x = []
y = []


for i in range(11):
    y.append(sin(i))
    x.append(i)
    print(i, y)



fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()