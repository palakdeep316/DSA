class Solution(object):
    def leftRightDifference(self, nums):
        l1=[]
        for i in range (0,len(nums)):
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            l=abs(left-right)
            l1.append(l)
        return l1