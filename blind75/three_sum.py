"""
Time of Start: 9:31 AM
Time at start solutioning:
Time at start coding: 9:42
time at testing:
time at submission:
"""

class Solution:
    """
    1. O(n^3) solution. find every number.
    [-1,0,1,2,-1,-4] => [-4 -1 -1 0 1 2]
    it's not sorted. 
    2. O(n^2) and O(n) extra space -> set + scan every possible pair.
    3. x + y + z = target
    """
    def three_sum(self, nums):
        sorted_nums = sorted(nums)
        three_sums = set()

        for i in range(len(sorted_nums)):
            j = i + 1
            k = len(sorted_nums)-1
            while j < k:
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
                    three_sums.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
                    continue
                elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > 0:
                    k -= 1
                elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] < 0:
                    j += 1
        new_list = list(three_sums)
        final_list = []
        for i in range(len(new_list)):
            final_list.append(list(new_list[i]))
        return final_list

if __name__ == '__main__':
    s = Solution()
    print(s.three_sum([-1,0,1,2,-1,-4]))
    print(s.three_sum([0,1,1]))
    print(s.three_sum([0,0,0]))
