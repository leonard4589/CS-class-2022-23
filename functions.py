def graph(x):
    y = (x**2)/4
    return y

def inverse(x):
    y = 2*(x**0.5)
    return y

x = []
y = []
z = []

for i in range(0, 11):
    x.append(i)
    y.append(graph(i))

print("x: ", x)
print("y: ", y)

for i in range(0, 11):
    z.append(inverse(i))

print("z: ", z)