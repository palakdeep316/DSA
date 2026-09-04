class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            maxi=max(nums[:i+1])
            mini=min(nums[i:])
            s=maxi-mini
            if s<=k:
               return i
        return -1