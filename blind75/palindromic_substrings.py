"""
Time of Start: 6:45 PM
Time at start solutioning: -
Time at start coding: 6:53
time at testing: 7:01
time at submission:
"""

"""
["abccbacc"]
global counter
for every index:
    is it a single origin palin
        for each part of the palin i need to have a counter -> add this to global counter
    is it a double origin palin
    for each part of the palin i need to have a counter -> add this to global counter
"""
class Solution:
    def palindromic_substrings(self, s):
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        global_count = 0
        for i in range(len(s)):
            global_count += self.isSingleOriginPalin(s, i)
            global_count += self.isDoubleOriginPalin(s, i-1, i)
        return global_count
        
    def isSingleOriginPalin(self, s, i):
        num_palins = 1
        j = i - 1
        k = i + 1
        while j >= 0 and k < len(s):
            if s[j] == s[k]:
                num_palins += 1
                k += 1
                j -= 1
            else:
                break
        return num_palins

    def isDoubleOriginPalin(self, s, i, j):
        num_palins = 0
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                num_palins += 1
                i -= 1
                j += 1
            else:
                break
        return num_palins

if __name__ == '__main__':
    s = Solution()
    print(s.palindromic_substrings("aaa"))
