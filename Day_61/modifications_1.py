# Double each element - Multiply every element by 2 and return the modified array
def modified_array(array):
    modified = []
    for i in array:
        i *= 2
        modified.append(i)
    return modified

arr = [1,2,3,4,5,6,7]
result = modified_array(arr)
print("doubled array :",result)
#time complexity O(n) and space complexity O(n)