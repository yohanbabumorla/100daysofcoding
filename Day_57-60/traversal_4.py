# Find the largest element - Return the maximum value in the array
def largest_element(array):
    largest = float('-inf')
    if not array:
        return None
    for i in array:
        if largest < i:
            largest = i
    return largest


arr = [2,4,7,3,6,8,23,56,34,67]
result = largest_element(arr)
print(f"\nThe largest element in an array is {result}")
#time complexity is O(n) and space complexity is O(1)