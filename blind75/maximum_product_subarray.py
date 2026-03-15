"""
Time of Start: 9:40
Time at start solutioning:
Time at start coding:
time at testing:
time at submission:
"""

class Solution:
    '''
    len(nums) == 1:
        return num[0]
    handle empty list.
    [2,3,-2,4]
    [-2,0,-1]
    [1,2,3,4,-2,-1,-2] => 1, 2, 6, 12, -6, 72, -2
    sorting - not going to work since order matters for subarray
    2 pointer:
        p1=0; p2=0; product = 2;
        p1=0; p2=1; product = 6; => max
        p1=0; p2=2; product = -12
        p1=1; p2=2 product = -6

     [2, 6, -2, 4] => max(6)   
------------------------------------
    '''
    def maxProduct(self, nums):
        products = [1] * len(nums)
        products[0] = nums[0]

        for i in range(len(nums)):
            pass