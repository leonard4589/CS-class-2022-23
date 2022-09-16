def slope(x1, y1, x2, y2):
    try:
        s = (y2 - y1)/(x2 - x1)
    except:
        s = None
    return s 

def yintercept(x1, x2, y1, y2):
    try:
        yintercept = -(slope(x1,y1,x2,y2)*x1) + y1 
    except:
        yintercept = None
    return yintercept 

x1 = 2
y1 = 5
x2 = 2
y2 = 10

print("Slope = ", slope(x1,y1,x2,y2))

print("y-intercept = ", yintercept(x1,x2,y1,y2))
