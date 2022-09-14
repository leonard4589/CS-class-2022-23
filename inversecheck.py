def fx(x):
    y = x**2/4
    return y 

def gx(x):
    y = 2*x**0.5
    return y 

#print(fx(2), gx(9)) # check to see if functions are working 

n = 2
print ("starting value: ", n)
b = fx(n)
print ("f(n): ", b)
c = gx(b)
print ("g(b): ", c)

if n == gx(b):
    print("Functions are inverse.")
else:
    (print("You failed."))
