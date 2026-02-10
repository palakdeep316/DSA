class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele=sd=0
        for i in nums:
            ele+=i
            while(i!=0):
                sd+=i%10
                i//=10
        return abs(ele-sd)

        