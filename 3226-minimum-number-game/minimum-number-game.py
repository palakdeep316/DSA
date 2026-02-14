class Solution(object):
    def numberGame(self, nums):
        arr=[]
        nums.sort()
        while(len(nums)>0):
            a=nums.pop(0)
            b=nums.pop(0)
            arr.append(b)
            arr.append(a)
        return arr