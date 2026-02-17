class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        lt = []
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                lt.append(nums[i])
        return lt