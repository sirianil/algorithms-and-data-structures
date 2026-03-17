"""
Time of Start: 9:41
Time at start solutioning:
Time at start coding:
time at testing:
time at submission:
"""

"""
[-2 1 -3 4 -1 2 1 -5 4]

current_sum = None;
global_max = float('-inf');
two pointers: p1 and p2 = 0
current_array => -2 => update global => -2 
p1=0 p2=1 => -1. (-1 > -2) => g=-1
p1=0 p2=-3 => -5 
[-2 1 -3 4 -1 2 1 -5 4]
-2 1 -2 4 3 5 6 1 5
[-2 1 -2 4 3 5 0 4]
"""
class Solution:
    def maxSubArray(self, nums):
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
        global_max = dp[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            global_max = max(global_max, dp[i])
        return global_max

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))