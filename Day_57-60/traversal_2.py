"""Find sum of all elements - Calculate and return the total sum of array elements"""
def sum_elements(array):
    total = 0
    for i in array:
        total += i

    return total


arr = [x for x in range(1,11) if x % 2 == 0]
result = sum_elements(arr)
print(result)
#time complexity O(n) and space complexity O(1)