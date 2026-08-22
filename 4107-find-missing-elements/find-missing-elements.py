class Solution(object):
    def findMissingElements(self, nums):
        new=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                new.append(i)
        return new