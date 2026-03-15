Instructions for myself:

This is the repository where i solve the Blind75 List for interview questions from Leetcode. https://leetcode.com/problem-list/wtbbziic/

I'll sort by Question ID and solve in that order.
I won't use a pen or paper, but will think out loud while making notes in the comments. I'll code in my VSCode IDE and once I've tested and satiified I'll paste it in Leetcode.

I'll spend 35-40 minutes for each question.
5 minutes: Understanding the problem
5-10 minutes: thinking through a solution, writing my thoughts in a comment, talking through the solution
15 minutes: Coding
5-10 minutes: Testing, edge cases and other optimizations


Skeleton to use at start of problem:
"""
Time of Start: 
Time at start solutioning:
Time at start coding:
time at testing:
time at submission:
"""

class Solution:
    def __init__(self):
        pass

if __name__ == '__main__':
    s = Solution()


When presented with a problem, see what patterns you can take advantage of:
1. will extra space to store things while processing help?
2. if extra space helps, then does quick look up in the extra space reduce processing time?
3. if extra space, does storing more data with the look up help? then use a map, else use a set. 
3. will rearannging data to take advantage of certain patterns help? if so will sorting help?
4. if the data is sorted, then systematiaclly manipulating 2 pointers may help - like increasing or decreasing depending on what value you are looking for.
5. if two pointers - how do you want to manipulate the pointers?
6. like would either end and working inward? or both in middle and working outwards work?
7. or starting together and incrementing only one until you reach a certain state help?
8. or a sliding window? keep only valid elements in a window and increment or decrement as required in the window.
9. for linkedLists, it is pretty standard. there will be pointer manipulation. either you move a slow and fast or move in a cycle
10. 

Notes:
there are 2 DP problems that i have the brute force solution for, that i need to learn the dp way.
1. pacific atlantic water
2. word break
3. maximum product subarray

I need more practise with backtracking solutions as well:
1. combination sum