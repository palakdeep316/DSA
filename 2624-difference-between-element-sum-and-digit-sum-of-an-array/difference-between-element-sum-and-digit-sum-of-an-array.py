class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele=0
        sd=0
        for i in nums:
            ele+=i
            while(i!=0):
                d=i%10
                sd+=d
                i/=10
        return abs(ele-sd)

        