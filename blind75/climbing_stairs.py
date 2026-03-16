class Solution:
    '''
    n steps -> to reach top.
    0 -> 0
    1 -> 1
    2 -> 2
    3 -> climb(1) + climb(2)
    4 -> climb(3) + climb(2)
    '''
    # index [0=step1, 1=step2, 2=step3, 3, ...... n-1=step n]
    # ways  [1, 2, , ......... n]
    def climbing_stairs(self, n):
        ways = [None] * n
        ways[0] = 1 #step 1
        ways[1] = 2 #step 2

        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.climbing_stairs(3))
