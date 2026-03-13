class Solution:
    def minSubArrayLen(self, target, nums):
        global_min = float('inf')
        
        p1 = p2 = 0
        w_len = 1
        w_sum = nums[0]

        while p1 <= p2 and p2 < len(nums):
            if w_len == 1 and  w_sum >= target:
                return 1
            
            if w_sum < target:
                p2 = p2 + 1
                w_len = w_len + 1
                w_sum = w_sum + nums[p2]
            elif w_sum >= target:
                global_min = w_len if global_min > w_len else global_min
                p1 = p1 + 1
                w_len = w_len - 1
                w_sum = w_sum - nums[p1]

        return global_min
    
if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))