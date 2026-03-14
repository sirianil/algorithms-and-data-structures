"""
Time of Start: 6:22 PM
Time at start solutioning:
Time at start coding: 6:33 PM
time at testing: 
time at submission: 6:40
"""

"""
integer array - height.
height = [1,8,6,2,5,4,8,3,7]
O(n^2) solution: compare every number with every number. multiply the min with the diff.
p1=0; p2=8; => 1*8 = 8;
p1=1; p2=8; -> 7*7 = 49; -> max
p1=1; p2=7; -> 3*8 = 24;
p1=1; p2=6 -> 8*5 = 40;
[1 1 1 1 1 1 1 1 4 4 9 1 2]
"""

"""
review:
i think you are getting a hang of things.
you thought of the solution, and once you had a clear solution you coded it fast.
you weren't sure if your solution would work for all cases, but you went
with the best solution you had based on the tag greedy.
"""
class Solution:
    def container_with_most_water(self, height):
        i, j = 0, len(height)-1
        max_water = 0
        while (i < j):
            current_area = min(height[i], height[j]) * (j-i)
            max_water = max(current_area, max_water)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water

if __name__ == '__main__':
    s = Solution()
    print(s.container_with_most_water([1,8,6,2,5,4,8,3,7]))
    print(s.container_with_most_water([1,1]))
    print(s.container_with_most_water([1,2,1,1]))
    print(s.container_with_most_water([1,2,1,8]))
