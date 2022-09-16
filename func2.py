def slope(x1, y1, x2, y2):
    s = (y2 - y1)/(x2 - x1)
    return s 

def yintercept(x1, x2, y1, y2):
    yintercept = -(slope(x1,y1,x2,y2)*x1) + y1 
    return yintercept 

x1 = 2
y1 = 10
x2 = 4
y2 = 10

if slope(x1,y1,x2,y2) == 0:
    print("Slope = None")
else:
    print("Slope = ", slope(x1,y1,x2,y2))
    
print("y-intercept = ", yintercept(x1,x2,y1,y2))
