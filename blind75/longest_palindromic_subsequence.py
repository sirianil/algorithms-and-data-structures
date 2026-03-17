"""
Time of Start: 
Time at start solutioning:
Time at start coding: 10:20
time at testing:
time at submission:
"""
'''
baebbbab
'''
'''
bbbab
for every index:
    isSingleOriginPalin(i):
    isDoubleOriginPalin(i, j): 
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        global_max = float('-inf')

        for i in range(l):
            global_max = max(global_max, self.isSingleOriginPalin(s, i))

            global_max = max(global_max, self.isDoubleOriginPalin(s, i, i-1))

            global_max = max(global_max, self.isDoubleOriginPalin(s, i, i+1))
        return global_max

    def isSingleOriginPalin(self, s, i):
        p1 = i - 1
        p2 = i + 1
        
        cur_len = 0
        while p1 >= 0 and p2 < len(s):
            


    
    def isDoubleOriginPalin(self, s, i, j):
        pass    