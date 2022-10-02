#4
#def squared(n):
    #x = float(n)
    #sn = x**2
    #return (sn)

#n = input("Enter a number: ")
#print(f"The number {n} squared is {squared(n)}")

#5
def area(x1, x2):
    y1 = float(x1)
    y2 = float(x2)
    a = y1*y2
    return (a)

def perimeter(x1, x2):
    y1 = float(x1)
    y2 = float(x2)
    p = (y1*2) + (y2*2)
    return (p)


x1 = input("Enter the width: ")
x2 = input("Enter the length: ")
print(f"The area of the rectangle is {area(x1, x2)} and the perimeter is {perimeter(x1, x2)}")
