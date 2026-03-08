class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        print("Entered")
        s = nums[0]
        m = nums[1]
        l = nums[2]

        for i in range(len(nums)):
            print("s is ", s)
            print("m is ", m)
            print("l is ", l)            
            if s < m and m < l:
                return True
                       
            print("i is", i)
            if s > nums[i]:
                l = m
                m = s
                s = nums[i]
                continue
            elif m > nums[i]:
                l = m
                m = nums[i]                
                continue
            elif l > nums[i]:
                l = nums[i]
                continue

        return False
