# rotate an array elements to the right by k positions
def rotate_array(array, k):
    k = k % len(array) # it handles k > n
    return array[-k:] + array[:-k]
    #time O(n) and space O(n)

def rotate_in_place(array,k):
    n = len(array)
    k %= n

    def reverse(nums,start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    reverse(array, 0 , n-1)
    reverse(array, 0, k-1)
    reverse(array, k, n-1)
    return array
    #time O(n) and space O(1)

arr = [1,2,3,4,5,6,7]
result =  rotate_in_place(arr, 3)
print(result)
