class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        ans=0
        for i in nums:
            while i>0:
                if i%10==digit:
                    ans+=1
                i//=10
        return ans