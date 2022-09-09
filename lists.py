# list;array:
costs = [10.00,
18.00,
18.00,
11.00,
17.50,
11.00,
17.50,
11.00,
17.50,
11.00,
30.00,
17.50,
20.50,
11.50,
6.50,
5.60,
7.50]
# average:
# total = 0

# for i in costs:
#     total = total + i
# print("total =", total)
# print("average =", total/17)

# max cost:
# maxVal = -999
# for i in costs:
#     if i > maxVal:
#         maxVal = i
# print(maxVal)

# min cost:
minVal = 999
for i in costs:
    if i < minVal:
        minVal = i
print(minVal)

