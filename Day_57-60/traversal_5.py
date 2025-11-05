#Find the smallest element - Return the minimum value in the array
def smallest_ele(array):
    if not array:
        return None
    smallest = array[0]
    for i in array:
        if i < smallest:
            smallest = i
    return smallest

arr = [2,4,7,3,6,8,23,56,34,67]
result = smallest_ele(arr)
print(f"\nThe smallest element in an array is {result}")
#time complexity is O(n) and space complexity is O(1)