# loop:
# for i in range (21):
#     print(i)

#while loop
# x = 0            #initialize
# while x <= 30:
#     print (x)
#     x = x + 1    #increment x
    
# 0-20 except if it is divisable by 5
# for i in range (21):
#     if i % 5 == 0:
#         print("-")
#     else:
#         print(i)

# prime v.s not prime
# x = 12  #tests one number at a time; change x to change the number that is being tested
# for i in range(2, x):
#     if x % i == 0:
#         print(i, "False")
#     else:
#         print(i, "True")

#an easier way to do it:
# n = 13
# isPrime = True
# for i  in range(2, n):
#     print(n, i, n%i)
#     if n%i == 0:
#         print(n, "is not a prime")
#         isPrime = False
#         break

# if isPrime == True:
#     print(n, "is a prime")

#first 30 numbers of the fibonacci sequence
#fn = (fn -1) + (fn - 2) n>1

# n = 30     #number of members

# f1 = 1     #initialization
# f2 = 1
# print(f1)
# print(f2)

# for i in range(2,n + 1):
#     fnew = f1 + f2   #calculate values
#     print(fnew)
#     f1 = f2    #update
#     f2 = fnew 

# values of function f(x) = x^2 - 3x + 4
for i in range(0,21):
    y = i**2 - 3*i + 4
    print(i, y)



   
