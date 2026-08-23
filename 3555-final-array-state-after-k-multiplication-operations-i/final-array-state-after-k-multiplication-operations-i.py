class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            m=nums.index(min(nums))
            nums[m]*=multiplier
        return nums
