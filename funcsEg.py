<<<<<<< HEAD
#f(x) = 2x^2 = x - 2
from operator import truediv


def q1(x):
    y = 2*x**2 + x - 2
    return y

#x = 5
#print (q1(x))

#for i in range(5):
    #x = input("Enter a number: ")
    #n = float(x)
    #print(q1(n))

doAgain = True

while doAgain:
    x = input("Enter a number: ")
    if x == "stop":
        doAgain = False
        print("done")
    else:
        n = float(x)
        print(q1(n)) 
    
=======
#f(x) = 2x^2 = x - 2



def q1(x):
    y = 2*x**2 + x - 2
    return y

#x = 5
#print (q1(x))

#for i in range(5):
    #x = input("Enter a number: ")
    #n = float(x)
    #print(q1(n))

doAgain = True

while doAgain:
    x = input("Enter a number: ")
    if x == "stop":
        doAgain = False
        print("done")
    else:
        n = float(x)
        print(q1(n)) 
    
>>>>>>> 5374128ffbf3196619554e939ee50346eb8166a9
