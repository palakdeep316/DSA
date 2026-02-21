class Solution(object):
    def smallestRangeI(self, nums, k):
        mn=min(nums)
        mx=max(nums)
        return max(0,(mx-mn-(2*k)))
        