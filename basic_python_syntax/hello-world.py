import math 

def initial_function():
    print ("Hello World!")

''' Prints the sign of the given number
Prints Number is positive or
Number is Negative or
Number is zero
'''
def print_sign(num):
    if num > 0 :
        print("Number is positive")
    elif num == 0:
        print("Number is zero")
    else:
        print("Number is negative")

def loop_array(nums):
    for i in range(len(nums)):
        print(nums[i])

def is_sorted(nums):
    last_num = None
    for i in range(len(nums)):
        if i != 0 and nums[i] < last_num:
            return "Array is not sorted"
        last_num = nums[i]
    return "Array is sorted"

def main():
    visited = [[False for i in range(2)] for i in range(2)]
    print(visited)
    # initial_function()
    # print_sign(-10)
    # loop_array([1, 2, 3, 4, 5, 6])
    # print(is_sorted([1]))

if __name__ == '__main__':
    main()
