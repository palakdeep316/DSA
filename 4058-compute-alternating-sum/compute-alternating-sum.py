class Solution(object):
    def alternatingSum(self, nums):
        sub=add=0
        for i in range(len(nums)):
            if i%2==0:
                add+=nums[i]
            else:
                sub+=nums[i]
        return add-sub