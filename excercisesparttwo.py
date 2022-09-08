#1.
# n = input("Enter your name: ")

# l = len(n)

# print(len)

# if len < 6:
#     print(f"{n}, your name is short.")
# else:
#     print(f"{n}, your name is long. It has {l} letters.")

#2.
# from cmath import pi


# def volumeCylinder(r,h):
#     r = float(r)
#     h = float(h)
#     v = (pi*r**2)*h
#     return (v)

# r = input("Enter the radius: ")
# h = input("Enter the height: ")
# print(f"The volume of the cylinder is {volumeCylinder(r,h)}")

#3.
# n = input("Enter a number: ")

# n = float(n)
# y = n/3

    
# if ( float(n) % 3) == 0:
#     print (f"{n} is divisable by 3. The answer is {y}")
# else:
#     print (f"{n} is not divisable by 3.")

#4.
o = input("What size would you like your drink to be today: ")
#a.
o = o.lower()  
#b.
o = o.strip ()
#c.
o = o.replace(" ", "")
#it could have also been: o = o.lower().strip().replace(" ", "")

if o == "venti":
    print("You probably should have something smaller.")
elif o == "tall":
    print("Do you mean a small?")
elif o == "grande":
    print("How nice!")
else:
    print("What are you talking about?")

