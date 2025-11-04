list1 = [1,4,3,2,7,6,5,9,8,0,23]
print(f"original list: {list1}")
i = 0
j = len(list1)-1
while i<j:
    list1[i], list1[j] = list1[j], list1[i]
    i += 1
    j -= 1
print(f"reversed list : {list1}")