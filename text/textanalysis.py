with open('terence.txt') as f:
    lines = f.readlines()


print ("Length: ", len(lines))
print ((lines[0][-2]))

lt = lines[0].strip().split(" ")
print (lt)
print(len(lt))