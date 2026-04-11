class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        new=[]
        for i in range(len(nums)):
            sum=0
            for j in range (len(nums)):
                if nums[i]>nums[j]:
                    sum+=1
            new.append(sum)
        return new