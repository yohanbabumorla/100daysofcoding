def merge_arrays(array1,array2):
    i = j = 0
    merged_array = []
    len_1 = len(array1)
    len_2 = len(array2)
    len_merged = len_1 + len_2
    while i < len_1 and j < len_2:
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
    merged_array.extend(array1[i:])
    merged_array.extend(array2[j:])
    return merged_array


arr1 = [1,3,5]
arr2 = [2,4,6]
result = merge_arrays(arr1,arr2)
print(result)

#time -> O(n) and space -> O(n) 