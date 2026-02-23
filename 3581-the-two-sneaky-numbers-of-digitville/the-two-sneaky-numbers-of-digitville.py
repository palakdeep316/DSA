class Solution(object):
    def getSneakyNumbers(self, nums):
        s=[]
        for i in nums:
            if nums.count(i)>1 and i not in s:
                s.append(i)
        return s