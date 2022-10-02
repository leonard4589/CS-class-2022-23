import matplotlib.pyplot as plt

x = []
y = []

for i in range(21):
    f = i**2 - 3*1 + 4
    x.append(i)
    y.append(f)

print (y)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()



