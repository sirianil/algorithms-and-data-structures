"""
Time of Start: 9:17
Time at start solutioning:
Time at start coding: 9:19
time at testing:
time at submission:
"""

class Solution:
    """
    Sort and check: O(nlogn)
    extra storage like a set - O(n) extra space.
    you can do one iteration - find min and max.
    then iterate again and check which number is not found in between that.
    """
    def missing_number(nums):
        nums_set = set(nums)
        for n in range(0, len(n)+1):
            if n not in nums_set:
                return n

if __name__ == '__main__':
    s = Solution()
    s.missing_number(nums)