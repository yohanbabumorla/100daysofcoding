#find the largest number in the list
#simple way
a1 = [2,4,21,4]
print(max(a1))

#logical way
a = [2,4,21,4]
temp = 0
for i in a:
    if i>temp:
        temp = i
print(temp)

