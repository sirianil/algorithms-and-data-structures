"""
Time of Start: 1:30
Time at start solutioning:
Time at start coding: 1:36 (first time coding a backtracking problem, going to take 15 mins for an attempt and then look at the code)
time at testing:
time at submission:
"""

'''
candidates = [2,3,6,7]
target = 7
7, [2,3,6,7]
5, [2,3,6,7]
3, [2,3,6,7]
1, [2,3,6,7]
1, [3,6,7]
1, [6,7]
1, [7] 
3, [3,6,7] => sum == 0 ==>

target -> number you're looking for
list -> valid nums you're considering

idx=0, comb=[], total=0
comb[2]; total=2
idx=1; comb=[] total=0



'''

class Solution:
    def combinationSum(self, candidates, target):
            
        res = []

        def make_combination(idx, comb, total):
            print("Considering combination ", comb, " and total is ", total)
            if total == target:
                res.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)

            return res

        return make_combination(0, [], 0)

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))