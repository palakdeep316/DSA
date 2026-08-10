class Solution(object):
    def concatWithReverse(self, nums):
        nums.extend(nums[::-1])
        return nums