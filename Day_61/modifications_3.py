# Replace negative with zero - Change all negative numbers in the array to 0
def change_to_zero(array):
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = 0
    return array


arr = [1,-3,4,-9,-3,3,7,8]
result = change_to_zero(arr)
print("The modified array: ",result)
#time complexity O(n) and space complexity O(1)