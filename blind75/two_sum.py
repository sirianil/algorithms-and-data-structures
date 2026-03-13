"""
Time of Start: 10:51 AM
Time at start solutioning: 10:53
Time at start coding: 10:55
time at testing: 11:00
time at submission: 11:06
"""
"""
Overall review: Good on timing and solution.  
Missed a key edge case because you didn't read the requirements well enough
"""

class Solution:
    def two_sum(self, nums, target):
        nums_dict = {nums[i] : i for i in range(len(nums))}

        for i, v in enumerate(nums):
            j = nums_dict.get((target-v), None)
            if j is not None and i != j:
                return i, nums_dict[(target-v)]
        
        return (-1,-1)

if __name__ == '__main__':
    s = Solution()
    print(s.two_sum([3,2,4], 6))
