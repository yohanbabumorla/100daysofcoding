list1 = [2,3,6,4,7,9,10,64,24]
max = list1[0]
min = list1[0]
for i in list1:
    if max < i:
        max = i
    if min > i:
        min = i
print(f"maximum element in the list is {max}")
print(f"minimum element in the list is {min}")