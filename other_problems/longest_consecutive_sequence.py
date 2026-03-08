def longest_consecutive_sequence(nums):
    print("Start iterating", nums)

    hs = set(nums)
    longest_seq = 0 
    current_seq = 1
    for i in range(len(nums)):
        current_num = nums[i] + 1
        while (current_num in hs):
            current_seq = current_seq + 1
            current_num = current_num + 1
        if current_seq > longest_seq:
            longest_seq = current_seq
        current_seq = 1
    return longest_seq        

def main():
    nums = []
    print(longest_consecutive_sequence(nums))

if __name__ == '__main__':
    main()