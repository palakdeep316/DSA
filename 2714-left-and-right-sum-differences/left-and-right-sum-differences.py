class Solution(object):
    def leftRightDifference(self, nums):
        l1=[]
        for i in range (0,len(nums)):
            l=abs(sum(nums[:i])-sum(nums[i+1:]))
            l1.append(l)
        return l1