def play_with_arrays():
    nums = [1, 2, 3, 5, 6, 8, 10, 12, 11, 15, 16]
    print(nums)

    length = len(nums)
    print("Length is ", length)

    first_slice = nums[:5] # End is exclusive
    print("First slice is ", first_slice)

    second_slice = nums[5:] # Start is inclusive
    print("Second slice is ", second_slice)

    middle_slice = nums[2:5] # [3, 5, 6]
    print("Middle slice is ", middle_slice)

'''
Edge Cases:
1. Empty array: return False
2. Array with single element: mid = 0; if single element is num, then found
'''

def binary_search(array, num):
    if len(array) == 0:
        return False
    mid = int(len(array)/2)
    if array[mid] == num:
        return True
    elif array[mid] > num:
        is_found = binary_search(array[:mid] , num)
        if is_found == True:
            return True
    else:
        return binary_search(array[mid+1:], num)
    return False

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = int(len(array)/2)
    first_array = merge_sort(array[:mid])
    second_array = merge_sort(array[mid:])
    merged_array = merge(first_array, second_array)
    print(merged_array)
    return merged_array

def merge(array1, array2):
    pointer1 = pointer2 = 0
    final_array = []    
    while(pointer1 != len(array1) and pointer2 != len(array2)):
        if(array1[pointer1] < array2[pointer2]):
            final_array.append(array1[pointer1])
            pointer1 += 1
        else:
            final_array.append(array2[pointer2])
            pointer2 += 1

    if pointer1 != len(array1):
        final_array.extend(array1[pointer1:])

    if pointer2 != len(array2):
        final_array.extend(array2[pointer2:])
    
    return final_array

def main():
    # play_with_arrays()
    print(binary_search([], 5))

if __name__ == '__main__':
    main()