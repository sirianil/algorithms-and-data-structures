class Solution:
    def findMin(self, nums):
        pass

    def findInflectionPoint(self, nums):
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return nums[0]

        mid = int(len(nums) / 2)
        print("Nums is ", nums, " Mid is ", mid)

        prev_i = mid - 1 if mid - 1 >= 0 else len(nums) - 1 #0
        next_i = mid + 1 if mid + 1 < len(nums) else 0 #0

        if nums[prev_i] > nums[mid] and nums[next_i] > nums[mid]:
            return nums[mid]

        if nums[0] > nums[mid]:
            return self.findInflectionPoint(nums[0:mid-1])
        else:
            return self.findInflectionPoint(nums[mid+1:])

if __name__ == '__main__':
    s = Solution()
    print(s.findInflectionPoint([3,4,5,1,2]))