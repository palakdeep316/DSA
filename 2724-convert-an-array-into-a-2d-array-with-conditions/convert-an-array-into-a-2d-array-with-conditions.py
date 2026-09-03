class Solution(object):
    def findMatrix(self, nums):
        ans=[]
        while len(nums)!=0:
            add = []
            remaining = []
            for j in range(len(nums)):
                if nums[j] not in add:
                    add.append(nums[j])
                else:
                    remaining.append(nums[j])
            nums = remaining
            ans.append(add)
        return ans