# Count even numbers - Count how many even numbers exist in the array

def count_even(array):
    count = 0
    for i in array:
        if i % 2 == 0:
            count += 1
    return count


arr = [2,4,7,3,6,8,23,56,34,67]
total = count_even(arr)
print(f"\nThe count of even elements in an array is {total}")
#time complexity O(n) and space complexity O(1)