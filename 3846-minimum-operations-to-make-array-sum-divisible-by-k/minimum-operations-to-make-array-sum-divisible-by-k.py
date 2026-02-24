class Solution(object):
    def minOperations(self, nums, k):
        if sum(nums)%k==0:
            return 0
        else:
            return (sum(nums)%k)