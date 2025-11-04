#simple way using python
a = [5,2,5,2,2]
for i in a:
    pat = i * '*'
    print(pat)

#logical way
b = [2,2,2,2,8,8]
print("                                                    ")
for i in b:
    count =""
    for j in range(i):
        count += "*"
    print(count)