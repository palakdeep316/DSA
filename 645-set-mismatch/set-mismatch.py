class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        s=sum(set(nums))
        duplicate=sum(nums)-s
        missing=n*(n+1)//2-s
        return [duplicate,missing]