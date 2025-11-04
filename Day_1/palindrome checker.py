#without using list methods
list1 = [1,2,"madara",4,"madara",2,1]
print(f"given list {list1}")
list2 = list1.copy()
i = 0
j = len(list1)-1
while i < j:
    list1[i], list1[j] = list1[j], list1[i]
    i += 1
    j -= 1
if list1 == list2:
    print("given list is a palindrome")
else:
    print("given list is not a palindrome")
