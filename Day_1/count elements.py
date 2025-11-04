list1 = [1,4,2,3,3,2,6,4,7,5,8,9,4,2,3,0,7,3,2]
given_element = int(input("enter an element to count: "))
count = 0
for i in list1:
    if given_element == i:
        count += 1
print(count)
