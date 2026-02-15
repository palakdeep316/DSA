class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in range (len(nums)):
            max=0
            while (nums[i]>0):
                nums[i]/=10
                max+=1
            if max%2==0:
                count+=1
        return count
