# Reverse an array - Reverse the order of elements in-place or create a new reversed array
def reverse(array):
    left = 0
    right = len(array)-1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array


arr = [1,2,3,4,5,6,7]
result = reverse(arr)
print("the reversed array:",result)
#time complexity O(n) space complexity 0(1)