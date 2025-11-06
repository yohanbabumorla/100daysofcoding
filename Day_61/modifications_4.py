# Swap first and last - Exchange the first and last elements of the array
def swap(array):
    if not array:
        return None
    array[0], array[len(array)-1] = array[len(array)-1], array[0]
    return array


arr = [1,2,3,4,5,6,7]
result = swap(arr)
print("The modified array: ",result)
#time complexity O(1) space complexity O(1)