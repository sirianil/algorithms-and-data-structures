class Solution:
    def maxOperations(self, nums, k):
        # edge cases
        if len(nums) == 0 or len(nums) == 1:
            return 0

        num_map = {}
        # populate map
        for i in range(len(nums)):
            if nums[i] in num_map:
                num_map[nums[i]] = num_map[nums[i]] + 1
            else:
                num_map[nums[i]] = 1

        second_set = set()
        # count pairs
        pair_counter = 0
        for num, num_count in num_map.items():
            if num in second_set or (k-num) in second_set:
                continue
                
            if (k-num) in num_map:
                print("num_count is ", num_count)
                print("num_count 2 is ", num_map[(k-num)])
                count = min(num_count, num_map[(k-num)])
                print("Count is ", count)
                pair_counter = pair_counter + count
                second_set.add(num)
                second_set.add(k-num)
                print("second set is ", second_set)
        
        return pair_counter