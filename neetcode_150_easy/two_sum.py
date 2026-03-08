class Solution:
    def twoSum(self, nums, target):
        numdict = {}
        for i in range(len(nums)):
            required = target-nums[i]
            if required in numdict:
                if numdict[required] > i:
                    return [i, numdict[required]]
                else:
                    return [numdict[required], i]
            else:
                numdict[nums[i]] = i
