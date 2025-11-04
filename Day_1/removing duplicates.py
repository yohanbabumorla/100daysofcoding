list1 = [1,2,1,2,5,4,3,6,7,8,5,7,8,4,3,2]
unique = []
for i in list1:
    if i in unique:
        continue
    else:
        unique.append(i)
print(unique)